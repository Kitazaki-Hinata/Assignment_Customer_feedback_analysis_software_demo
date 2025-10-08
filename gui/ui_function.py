'''Slot signals of widgets in ui_mainwindow'''

# python package
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image, ImageQt
from transformers import pipeline

# local module
from model_trainer.text_model_trainer import BERTTrainer
from model_trainer.pic_model_trainer import ResNet50DefectDetector
from gui.console import Console




class Ui_function(object):
    def __init__(self, software_widget):
        self.main_window = software_widget
        self.console = Console(self.main_window)

    def get_img(self):
        '''get image from local, return qt_image as parameter'''
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Select Image", ".", "Image Files (*.jpg *.png)")
        if not file_path:
            return
        self.img = Image.open(file_path)
        qt_img = ImageQt.ImageQt(self.img)
        pixmap = QPixmap.fromImage(qt_img).scaled(
            432,
            184,
            Qt.AspectRatioMode.KeepAspectRatio
        )
        self.main_window.picture_label.setPixmap(pixmap)
        self.console.console_writing("Image selected successfully")
        self.file_path = file_path

    def text_analyse(self, if_aggregate=False):
        '''text analysis slot
        if_aggregate : whether reasoning together with picture'''
        text = self.main_window.text_enter.toPlainText()
        if text == "":
            return
        self.text_analyser = BERTTrainer(main_window = self.main_window)

        # using model analyser in text_model_trainer.py
        model = pipeline("sentiment-analysis")
        model = model(text)
        self.console.console_writing("Text analysing via self-trained model and pipeline")

        # pipeline model
        predictions_pipe, confidences_pipe = model[0]["label"], model[0]["score"]
        label_pipe_map = {"NEGATIVE" : -1, "NEUTRAL": 0, "POSITIVE": 1}
        prediction_pipe_num : int = label_pipe_map[predictions_pipe]

        # self model
        predictions_self, confidences_self = self.text_analyser.text_analyser(text)
        predictions_self : int = predictions_self[0]
        confidences_self : float = confidences_self[0]
        label_map = {0: -1, 1: 0, 2: 1}   # convert 0, 1, 2 into -1, 0, 1 for future calculations
        predictions_self : int = label_map[predictions_self]

        # compute out final confidence and predictions
        weight_avg_confidence : float = (
            prediction_pipe_num * confidences_pipe +
            predictions_self * confidences_self
        )
        if weight_avg_confidence > 0.2:
            final_prediction : int = 2
        elif weight_avg_confidence < -0.2:
            final_prediction : int = 0
        else:
            final_prediction : int = 1

        final_confidence = abs(weight_avg_confidence)

        # then output text and show in the label widget
        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        self.console.console_writing("Text Reasoning is Finished")
        if not if_aggregate:
            result_text =  (
                f"Text Sentiment Reasoning Result:\n"
                f"Text: {text}\n"
                f"Predict: {label_map[final_prediction]} (Confidence: {final_confidence:.4f})"
            )
            self.main_window.result_label.setText(result_text)
        else:
            return label_map[final_prediction], final_confidence

    def picture_analyse(self, img_path = None, if_aggregate=False):
        '''picture analysis slot
        if_aggregate : whether reasoning together with text sentiment'''
        if img_path is None:
            return

        self.picture_analyser = ResNet50DefectDetector(main_window = self.main_window)

        # detect fault
        result :  dict = self.picture_analyser.detect_defects(img_path, threshold=0.5)
        if result and not if_aggregate:
            # result output area
            status = "Have problem" if result['has_defect'] else "Normal"
            self.main_window.result_label.setText(
                f"Picture Defect Detection Result:\n"
                f"Detect Result: {status}\n"
                f"Abnormal score: {result['defect_score']:.4f}"
            )
            print(f"Detect Result: {status}")
            print(f"Abnormal score: {result['defect_score']:.4f}")
            self.console.console_writing("Picture : Fault detect successful")
        elif result and if_aggregate:
            status = "Have problem" if result['has_defect'] else "Normal"
            return status, result['defect_score']


    def aggregate_analyse(self, img_path = None):
        '''reasoning both text and picture'''
        try:
            text_label, text_confidence = self.text_analyse(if_aggregate=True)
            pic_label, pic_confidence = self.picture_analyse(img_path = img_path, if_aggregate=True)
        except Exception as e:
            self.console.console_writing(f"Error : {e}")
            print("Error : " + {e})
            return

        if text_label and text_confidence and pic_label and pic_confidence:
            self.main_window.result_label.setText(
                f"Text Sentiment Reasoning Result:\n"
                f"Text Sentiment Result: {text_label} "
                f"Text Reasoning Confidence: {text_confidence:.4f})\n"
                f"Picture Detect Result: {pic_label}\n"
                f"Picture Detect Abnormal score: {pic_confidence:.4f}"
            )
            self.console.console_writing("Finished all process")

    def clear_result(self):
        '''clear text in console and result widget'''
        self.main_window.console.setText("")
        self.main_window.result_label.setText("Result will be displayed here")
