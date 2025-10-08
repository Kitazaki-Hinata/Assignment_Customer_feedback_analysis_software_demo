import cv2
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
from torchvision import models
from torchvision.models.resnet import ResNet50_Weights
from gui.console import Console
import os

class ResNet50DefectDetector:
    def __init__(self, num_classes=2, device="cuda", main_window = None):
        """Use ResNet50 to detect"""
        self.main_window = main_window
        self.device = device
        self.num_classes = num_classes
        current_file_path = os.path.abspath(os.path.dirname(__file__))
        self.console = Console(self.main_window)

        # model path
        self.model_path = os.path.join(current_file_path, "..", 'model', "resnet50_defect.pth")

        # initialize
        self.model = self._create_model()

        if os.path.exists(self.model_path):
            self._load_model_weights()
            self.console.console_writing(f"Loaded trained weights from {self.model_path}")
        else:
            self.console.console_writing("No pre-trained weights found. Using ImageNet pre-trained weights.")

        self.model.to(device)
        self.model.eval()

        # 图像预处理
        self.transform = ResNet50_Weights.IMAGENET1K_V2.transforms()
        self.console.console_writing("Image preprocessing pipeline initialized.")
        print(f"ResNet50 Defect Detector loaded successfully on {device}")

    def _create_model(self):
        model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)

        # detect  fault
        num_features = model.fc.in_features
        model.fc = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(num_features, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, self.num_classes)
        )

        return model

    def _load_model_weights(self):
        try:
            checkpoint = torch.load(self.model_path, map_location=self.device)
            if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
                self.model.load_state_dict(checkpoint['model_state_dict'])
            else:
                self.model.load_state_dict(checkpoint)
        except Exception as e:
            self.console.console_writing("Error loading model weights.")
            print(f"Error loading model weights: {e}")
            print("Using ImageNet pre-trained weights instead.")

    def load_and_preprocess_image(self, image_path):
        if isinstance(image_path, str):
            image = Image.open(image_path).convert("RGB")
        else:
            image = image_path

        image_tensor = self.transform(image)
        image_np = np.array(image)

        return image_tensor, image_np

    def detect_defects(self, image_path, threshold=0.5):
        try:
            # pre process image data source
            image_tensor, original_image = self.load_and_preprocess_image(image_path)
            input_batch = image_tensor.unsqueeze(0).to(self.device)

            # reasoning
            with torch.no_grad():
                outputs = self.model(input_batch)
                probabilities = torch.softmax(outputs, dim=1)
                defect_prob = probabilities[0, 1].item()  # assume, defect class is 1

            # create anomaly map
            anomaly_map = self._generate_anomaly_map(input_batch)

            # mask
            pred_mask = (anomaly_map > threshold * 255).astype(np.uint8)

            result = {
                'has_defect': defect_prob > threshold,
                'defect_score': defect_prob,
                'defect_class': torch.argmax(outputs, dim=1).item(),
                'all_probabilities': probabilities.cpu().numpy()[0],
                'anomaly_map': anomaly_map,
                'pred_mask': pred_mask,
                'image_size': original_image.shape[:2]
            }

            return result

        except Exception as e:
            self.console.console_writing("Error during defect detection.")
            print(f"Error during defect detection: {e}")
            return None

    def _generate_anomaly_map(self, input_batch):
        try:
            activation = {}

            def get_activation(name):
                def hook(model, input, output):
                    activation[name] = output.detach()
                return hook

            hook = self.model.layer4.register_forward_hook(get_activation('layer4'))

            with torch.no_grad():
                _ = self.model(input_batch)

            hook.remove()

            features = activation['layer4']
            heatmap = torch.mean(features, dim=1)[0]
            heatmap = torch.nn.functional.relu(heatmap)

            heatmap = heatmap.cpu().numpy()
            heatmap = (heatmap - heatmap.min()) / (heatmap.max() - heatmap.min() + 1e-8)
            heatmap = (heatmap * 255).astype(np.uint8)

            heatmap = cv2.resize(heatmap, (224, 224))
            heatmap = cv2.resize(heatmap, (input_batch.shape[3], input_batch.shape[2]))

            return heatmap

        except Exception as e:
            self.console.console_writing(f"Error generating anomaly map. {e}")
            print(f"Error generating anomaly map: {e}")
            return np.zeros((224, 224), dtype=np.uint8)
