# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_software_widget(object):
    def setupUi(self, software_widget):
        if not software_widget.objectName():
            software_widget.setObjectName(u"software_widget")
        software_widget.resize(900, 700)
        software_widget.setMinimumSize(QSize(900, 700))
        software_widget.setMaximumSize(QSize(900, 700))
        software_widget.setStyleSheet(u"background : #dddddd;")
        self.verticalLayout = QVBoxLayout(software_widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.software_title = QLabel(software_widget)
        self.software_title.setObjectName(u"software_title")
        self.software_title.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.software_title.setFont(font)
        self.software_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.software_title)

        self.input_area = QWidget(software_widget)
        self.input_area.setObjectName(u"input_area")
        self.input_area.setMaximumSize(QSize(16777215, 100000))
        self.horizontalLayout = QHBoxLayout(self.input_area)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_area = QWidget(self.input_area)
        self.text_area.setObjectName(u"text_area")
        self.text_area.setMaximumSize(QSize(450, 16777215))
        self.text_area.setStyleSheet(u"background:#eeeeee")
        self.verticalLayout_2 = QVBoxLayout(self.text_area)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_title = QLabel(self.text_area)
        self.text_title.setObjectName(u"text_title")
        self.text_title.setMinimumSize(QSize(0, 20))
        self.text_title.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.text_title.setFont(font1)
        self.text_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_title)

        self.text_enter = QPlainTextEdit(self.text_area)
        self.text_enter.setObjectName(u"text_enter")
        self.text_enter.setMaximumSize(QSize(10000, 10000))
        self.text_enter.setStyleSheet(u"background: #ffffff;")

        self.verticalLayout_2.addWidget(self.text_enter)

        self.widget = QWidget(self.text_area)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(10000, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_analyse_btn = QPushButton(self.widget)
        self.text_analyse_btn.setObjectName(u"text_analyse_btn")

        self.horizontalLayout_2.addWidget(self.text_analyse_btn)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.text_area)

        self.picture_area = QWidget(self.input_area)
        self.picture_area.setObjectName(u"picture_area")
        self.picture_area.setMinimumSize(QSize(450, 0))
        self.picture_area.setMaximumSize(QSize(450, 16777215))
        self.picture_area.setStyleSheet(u"background: #eeeeee;")
        self.verticalLayout_3 = QVBoxLayout(self.picture_area)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pic_title = QLabel(self.picture_area)
        self.pic_title.setObjectName(u"pic_title")
        self.pic_title.setMinimumSize(QSize(0, 20))
        self.pic_title.setMaximumSize(QSize(16777215, 20))
        self.pic_title.setFont(font1)
        self.pic_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.pic_title)

        self.picture_label = QLabel(self.picture_area)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setStyleSheet(u"color : #aaaaaa;")
        self.picture_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.picture_label)

        self.picture_btn_w = QWidget(self.picture_area)
        self.picture_btn_w.setObjectName(u"picture_btn_w")
        self.picture_btn_w.setMinimumSize(QSize(0, 50))
        self.picture_btn_w.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.picture_btn_w)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_picture = QPushButton(self.picture_btn_w)
        self.select_picture.setObjectName(u"select_picture")

        self.horizontalLayout_3.addWidget(self.select_picture)

        self.pic_analyse_btn = QPushButton(self.picture_btn_w)
        self.pic_analyse_btn.setObjectName(u"pic_analyse_btn")

        self.horizontalLayout_3.addWidget(self.pic_analyse_btn)


        self.verticalLayout_3.addWidget(self.picture_btn_w)


        self.horizontalLayout.addWidget(self.picture_area)


        self.verticalLayout.addWidget(self.input_area)

        self.result_widget = QWidget(software_widget)
        self.result_widget.setObjectName(u"result_widget")
        self.result_widget.setStyleSheet(u"background : #eeeeee;")
        self.horizontalLayout_4 = QHBoxLayout(self.result_widget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.result_btn_area = QWidget(self.result_widget)
        self.result_btn_area.setObjectName(u"result_btn_area")
        self.verticalLayout_4 = QVBoxLayout(self.result_btn_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.result_btn_area)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.analyse_all = QPushButton(self.result_btn_area)
        self.analyse_all.setObjectName(u"analyse_all")
        self.analyse_all.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.analyse_all)

        self.clear_result = QPushButton(self.result_btn_area)
        self.clear_result.setObjectName(u"clear_result")
        self.clear_result.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.clear_result)

        self.console = QLabel(self.result_btn_area)
        self.console.setObjectName(u"console")
        self.console.setMinimumSize(QSize(292, 149))
        self.console.setMaximumSize(QSize(292, 149))
        self.console.setStyleSheet(u"background : #dddddd; padding : 10px;")
        self.console.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.console)


        self.horizontalLayout_4.addWidget(self.result_btn_area)

        self.result_label = QLabel(self.result_widget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(550, 260))
        self.result_label.setMaximumSize(QSize(550, 16777215))
        self.result_label.setStyleSheet(u"background : white; padding : 10px;")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_4.addWidget(self.result_label)


        self.verticalLayout.addWidget(self.result_widget)


        self.retranslateUi(software_widget)

        QMetaObject.connectSlotsByName(software_widget)
    # setupUi

    def retranslateUi(self, software_widget):
        software_widget.setWindowTitle(QCoreApplication.translate("software_widget", u"Customer Feedback Analysis Software", None))
        self.software_title.setText(QCoreApplication.translate("software_widget", u"Customer Feedback Analysis Software (Demo)", None))
        self.text_title.setText(QCoreApplication.translate("software_widget", u"Text Analysis Working Area", None))
        self.text_enter.setPlaceholderText(QCoreApplication.translate("software_widget", u"Please enter your text here", None))
        self.text_analyse_btn.setText(QCoreApplication.translate("software_widget", u"AI Analysis Text Only", None))
        self.pic_title.setText(QCoreApplication.translate("software_widget", u"Picture Analysis Working Area", None))
        self.picture_label.setText(QCoreApplication.translate("software_widget", u"Picture will be shown here", None))
        self.select_picture.setText(QCoreApplication.translate("software_widget", u"Browse...", None))
        self.pic_analyse_btn.setText(QCoreApplication.translate("software_widget", u"AI Analysis Picture Only", None))
        self.label.setText(QCoreApplication.translate("software_widget", u"Result Working Area", None))
        self.analyse_all.setText(QCoreApplication.translate("software_widget", u"Analyse all", None))
        self.clear_result.setText(QCoreApplication.translate("software_widget", u"Clear Console and Result", None))
        self.console.setText(QCoreApplication.translate("software_widget", u"<html><head/><body><p>Console Information will be displayed here</p></body></html>", None))
        self.result_label.setText(QCoreApplication.translate("software_widget", u"Result will be displayed here", None))
    # retranslateUi

