'''model trainer and reasoning script, incl. BERT trainer class'''

print("Importing packages, please wait...")
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, f1_score
import warnings
warnings.filterwarnings('ignore')


class TextClassificationDataset(Dataset):
    '''
    Package the text data and its corresponding labels into the PyTorch dataset format.
    Perform tokenization on the text to prepare for model training.
    '''
    def __init__(self, texts : list[str], labels : list[int], tokenizer, max_length : int=128):
        '''
        :param texts: texts of training data
        :param labels: label of sentiment, 0 = Negative, 1 = Neutral, 2 = Positive
        :param tokenizer: function, separate texts into tokens(single words)
        :param max_length: max length per data, if text exceeds, then cut texts into pieces
        '''

        self.texts :  list[str] = texts
        self.labels:  list[int] = labels   # list with 0, 1, 2
        self.tokenizer = tokenizer
        self.max_length : int = max_length

    def __len__(self):
        # return total num of samples
        return len(self.texts)

    def __getitem__(self, idx) -> dict:
        text : str = str(self.texts[idx])
        label = self.labels[idx]

        # using tokenizer to do pretraining
        encoding:  dict = self.tokenizer(
            text,
            truncation=True,    # whether cut text into pieces
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'   # return pytorch tensors
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),   # preprocessed text, after tokenizer
            'attention_mask': encoding['attention_mask'].flatten(),   # attention mask
            'labels': torch.tensor(label, dtype=torch.long)   # label->pytorch tensor
        }


class BERTTrainer:
    '''BERT trainer, including training and predicting'''
    def __init__(self, main_window = None, model_name='bert-base-uncased', num_labels=3, max_length=128):
        self.main_window = main_window
        self.model_name : str = model_name
        self.num_labels : int = num_labels
        self.max_length : int = max_length
        print("Enabled CUDA : " + str(torch.cuda.is_available()))   # test whether CUDA is available, faster to use GPU
        self.device : torch.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # initialize model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=num_labels
        )
        self.model.to(self.device)

    def prepare_data(self, train_texts, train_labels, val_texts=None, val_labels=None, batch_size=16):
        # prepare train_dataset and verify data
        train_dataset = TextClassificationDataset(
            train_texts, train_labels, self.tokenizer, self.max_length
        )
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

        # Validation set initialization
        # Check if validation texts and labels are provided
        if val_texts is not None and val_labels is not None:
            val_dataset = TextClassificationDataset(
                val_texts, val_labels, self.tokenizer, self.max_length
            )
            self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
        else:
            self.val_loader = None

    def train(self, epochs=3, learning_rate=2e-5):
        optimizer = AdamW(self.model.parameters(), lr=learning_rate)
        total_steps = len(self.train_loader) * epochs
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=0,
            num_training_steps=total_steps
        )

        # loop for training
        self.model.train()
        for epoch in range(epochs):
            total_loss = 0
            for batch in self.train_loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                # forward propagation
                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    labels=labels
                )

                loss = outputs.loss
                total_loss += loss.item()

                # backward propagation
                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
                optimizer.step()
                scheduler.step()

            avg_loss = total_loss / len(self.train_loader)

            # verify, using method evaluate
            if self.val_loader:
                val_accuracy, val_f1 = self.evaluate()
                print(f'Finished : Epoch {epoch+1}/{epochs}')
                print(f'Current Training Loss : {avg_loss:.4f}')
                print(f'Validation Accuracy : {val_accuracy:.4f}, F1: {val_f1:.4f}')
            else:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}')
            print('-' * 45)    # separate line

    def evaluate(self):
        if not self.val_loader:
            return None, None

        self.model.eval()
        predictions = list()
        true_labels = list()

        with torch.no_grad():
            for batch in self.val_loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask
                )

                _ , preds = torch.max(outputs.logits, dim=1)
                predictions.extend(preds.cpu().tolist())
                true_labels.extend(labels.cpu().tolist())

        accuracy = accuracy_score(true_labels, predictions)
        f1 = f1_score(true_labels, predictions, average='weighted')

        self.model.train()
        return accuracy, f1


    # -----------------------------------------------
    # reasoning part

    def text_analyser(self, texts):
        '''reasoning part, after model is trained.
        This is used in ui function, input text, output sentiment'''

        # init console class, print useful info in console widget
        from gui.console import Console
        self.console = Console(self.main_window)

        # start reasoning
        self.console.console_writing("Start Reasoning...")
        self.model.eval()
        predictions = []
        confidences = []

        with torch.no_grad():
            for text in texts:
                encoding = self.tokenizer(
                    text,
                    truncation=True,
                    padding='max_length',
                    max_length=self.max_length,
                    return_tensors='pt'
                )

                input_ids = encoding['input_ids'].to(self.device)
                attention_mask = encoding['attention_mask'].to(self.device)

                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask
                )

                probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
                confidence, predicted_class = torch.max(probs, dim=1)

                predictions.append(predicted_class.cpu().item())
                confidences.append(confidence.cpu().item())

        return predictions, confidences

    def save_model(self, save_path):
        '''save model'''
        self.model.save_pretrained(save_path)
        self.tokenizer.save_pretrained(save_path)
        print(f"Model saved to {save_path}")

