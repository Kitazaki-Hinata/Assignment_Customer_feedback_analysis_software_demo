'''main entrance for model training'''

import os
import pandas as pd
from model_trainer.text_model_trainer import BERTTrainer

def main(text_folder, file_type='txt'):
    # separate text and label in a text file
    texts : list = list()
    labels : list = list()

    if file_type == "txt":
        for file in os.listdir(text_folder):
            file_path = os.path.join(text_folder, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.rstrip()
                    texts.append(line[:-2])
                    labels.append(int(line[-1]))
            if texts and labels:
                print("Data prepared successfully!")
            else:
                print("Failed to prepare data!")
                return

    elif file_type == "xlsx":
        for file in os.listdir(text_folder):
            if file.endswith('.xlsx'):
                file_path = os.path.join(text_folder, file)
                try:
                    df = pd.read_excel(file_path, engine='openpyxl')
                    num = 0
                    for index, row in df.iterrows():
                        try:
                            num += 1
                            text_val = str(row["Review"])
                            label_val = int(row["Label"])
                            texts.append(text_val)
                            labels.append(label_val)
                            print(num)
                        except:
                            pass
                except:
                    pass


    # separate train data and verify data
    split_idx = int(0.8 * len(texts))
    train_texts, val_texts = texts[:split_idx], texts[split_idx:]
    train_labels, val_labels = labels[:split_idx], labels[split_idx:]

    # initialize trainer class
    print("Initializing BERT trainer")
    trainer = BERTTrainer(
        model_name='bert-base-uncased',  # model name
        num_labels=3,  # 3 data set: 0, 1, 2
        max_length=128
    )

    # prepare data
    trainer.prepare_data(
        train_texts=train_texts,
        train_labels=train_labels,
        val_texts=val_texts,
        val_labels=val_labels,
        batch_size=8
    )

    # start training, using BERT class in text model trainer.py
    print("Start training...")
    trainer.train(epochs=12, learning_rate=2e-5)

    # save model
    current_file_path = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(current_file_path, "..", 'model')
    trainer.save_model(model_path)


if __name__ == "__main__":
    text_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "dataset", "Sentiment Labelled Sentences Data Set")
    main(text_folder, file_type='txt')