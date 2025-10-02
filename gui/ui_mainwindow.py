''' GUI settings'''

from PySide6.QtWidgets import QWidget
from gui.ui_function import Ui_function
from gui.ui_main import Ui_software_widget



class Demo_gui(QWidget, Ui_software_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui_function = Ui_function(self)

        # picture area button event
        self.qt_img = self.select_picture.clicked.connect(self.ui_function.get_img)  # return image file
        self.pic_analyse_btn.clicked.connect(lambda : self.ui_function.picture_analyse(self.qt_img))

        # text area button event
        self.text_analyse_btn.clicked.connect(self.ui_function.text_analyse)

        # result area button event
        self.clear_result.clicked.connect(self.ui_function.clear_result)


