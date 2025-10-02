'''Slot signals of widgets in ui_mainwindow'''

# python package
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image, ImageQt

# local module
from model_trainer.text_model_trainer import BERTTrainer
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
        return qt_img

    def text_analyse(self):
        '''text analysis slot'''
        text = self.main_window.text_enter.toPlainText()
        self.text_analyser = BERTTrainer(main_window = self.main_window)

        # using model analyser in text_model_trainer.py
        predictions, confidences = self.text_analyser.text_analyser(text)

        prediction = predictions[0]
        confidence = confidences[0]

        # then output text and show in the label widget
        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        result_text =  f'''
            Text Sentiment Reasoning Result:\n
            Text: {text}\n
            Predict: {label_map[prediction]} (Confidence: {confidence:.4f})
        '''
        self.main_window.result_label.setText(result_text)
        self.console.console_writing("Reasoning is Finished")

    def picture_analyse(self, qt_img = None):
        '''picture analysis slot'''
        pass

    def clear_result(self):
        '''clear text in console and result widget'''
        self.main_window.console.setText("")
        self.main_window.result_label.setText("Result will be displayed here")

    def return_main_window(self):
        return self.main_window