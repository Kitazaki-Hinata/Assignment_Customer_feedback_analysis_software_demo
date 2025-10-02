'''demo of the AI analysis part'''

from PySide6.QtWidgets import QApplication
from gui.ui_mainwindow import Demo_gui


if __name__ == '__main__':
    app = QApplication([])
    window = Demo_gui()
    window.show()
    app.exec()
