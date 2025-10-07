import cv2
import numpy as np
from PIL import Image
import torch
from anomalib.models import Patchcore
from anomalib.deploy import TorchInferencer
from anomalib.models import get_model
from pathlib import Path
import os

class DefectDetector:
    def __init__(self, model_name="patchcore", device="cuda"):
        """model_name : include "patchcore", "efficientad", "cflow" ..."""
        self.device = device
        self.model_name = model_name
        self.model = get_model(self.model_name)
        current_file_path = os.path.abspath(os.path.dirname(__file__))
        self.model_path = os.path.join(current_file_path, "..", 'model', "patchcore_mvtec.pth")

        # save model weight if there's no such file
        torch.save(self.model.state_dict(),  self.model_path)

        # load model
        self.inferencer = TorchInferencer(
            path=self.model_path,
            device=device,
        )

        print(f"{model_name} loaded successfully")

    def load_and_preprocess_image(self, image_path):
        """load model"""
        if isinstance(image_path, str):
            image = Image.open(image_path).convert("RGB")
        else:
            image = image_path

        image_np = np.array(image)
        return image_np

    def detect_defects(self, image_path, threshold=0.5):
        """
        Args:
            image_path: path of image
        Returns:
            dict: include result dict
        """
        try:
            # deal with data
            image = self.load_and_preprocess_image(image_path)

            # reasoning
            predictions = self.inferencer.predict(image=image)

            # result
            result = {
                'has_defect': predictions.pred_score > threshold,
                'defect_score': float(predictions.pred_score),
                'anomaly_map': predictions.anomaly_map,
                'pred_mask': predictions.pred_mask,
                'image_size': predictions.image_size
            }

            return result

        except Exception as e:
            print(f"Error: {e}")
            return None





