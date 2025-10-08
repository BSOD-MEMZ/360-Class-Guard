# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QIcon,
    QPixmap)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox, QFrame,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1290, 681)
        Form.setStyleSheet(u"background-color: #FFFFFF;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 690, 60))
        self.frame.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(68, 244, 160, 255), stop:1 rgba(86,178,172, 255));")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 10, 191, 41))
        self.label_2.setStyleSheet(u"background: none;\n"
"color :#FFFFFF;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 191, 41))
        self.label.setStyleSheet(u"background: none;\n"
"color :#FFFFFF;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 40, 40))
        self.label_6.setStyleSheet(u"background: none;")
        self.label_6.setPixmap(QPixmap(u"assets/logo.png"))
        self.label_6.setScaledContents(True)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(580, 16, 100, 32))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(77,116,212, 255), stop:1 rgba(77,153,212, 255));\n"
"border: 1px solid #FFFFFF;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33,81,102, 255), stop:1 rgba(33,59,102, 255));\n"
"color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"assets/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.Setting = QPushButton(self.frame)
        self.Setting.setObjectName(u"Setting")
        self.Setting.setGeometry(QRect(430, 0, 61, 61))
        self.Setting.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: none;\n"
"	border-width: 0px 0px 0px 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid rgba(255, 255, 255, 60);\n"
"	background: rgba(0, 0, 0, 10);\n"
"	border-width: 0px 1px 0px 1px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 60));\n"
"	border-width: 0px 1px 0px 1px;\n"
"}\n"
"QPushButton:checked{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 40));\n"
"	border-width: 0px 1px 0px 1px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Setting.setIcon(icon1)
        self.Setting.setIconSize(QSize(32, 32))
        self.Setting.setCheckable(True)
        self.Setting.setChecked(True)
        self.Setting.setAutoExclusive(True)
        self.Setting.setFlat(False)
        self.TextSetting = QPushButton(self.frame)
        self.TextSetting.setObjectName(u"TextSetting")
        self.TextSetting.setGeometry(QRect(490, 0, 61, 61))
        self.TextSetting.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: none;\n"
"	border-width: 0px 0px 0px 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid rgba(255, 255, 255, 60);\n"
"	background: rgba(0, 0, 0, 10);\n"
"	border-width: 0px 1px 0px 1px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 60));\n"
"	border-width: 0px 1px 0px 1px;\n"
"}\n"
"QPushButton:checked{\n"
"	border: 1px solid rgba(255, 255, 255, 120);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 40));\n"
"	border-width: 0px 1px 0px 1px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"assets/text.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TextSetting.setIcon(icon2)
        self.TextSetting.setIconSize(QSize(32, 32))
        self.TextSetting.setCheckable(True)
        self.TextSetting.setAutoExclusive(True)
        self.TextSetting.setFlat(False)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 390, 690, 41))
        self.frame_2.setStyleSheet(u"background-color: #FFFAD6;\n"
"border: 1px solid #D1D1D1;\n"
"border-width: 1px 0px 0px 0px;\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 681, 21))
        self.label_3.setStyleSheet(u"background: none;\n"
"color :#000000;\n"
"border: none;")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 140, 181, 171))
        self.label_5.setPixmap(QPixmap(u"assets/decoration.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 80, 211, 51))
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setTextFormat(Qt.TextFormat.RichText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 350, 140, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #00CA72;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00BF6C;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #007B45;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"assets/kill.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 350, 140, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #00CA72;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00BF6C;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #007B45;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"assets/dismiss.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(540, 350, 140, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: #00CA72;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00BF6C;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #007B45;\n"
"	color: #FFFFFF;\n"
"	border-radius: 6px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"assets/debug.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 80, 431, 221))
        self.NormalSettingWindow = QVBoxLayout(self.verticalLayoutWidget)
        self.NormalSettingWindow.setObjectName(u"NormalSettingWindow")
        self.NormalSettingWindow.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setStyleSheet(u"background: none;")
        self.checkBox_6.setChecked(True)

        self.NormalSettingWindow.addWidget(self.checkBox_6)

        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setStyleSheet(u"background: none;")
        self.checkBox_8.setChecked(True)

        self.NormalSettingWindow.addWidget(self.checkBox_8)

        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setStyleSheet(u"background: none;")
        self.checkBox_7.setChecked(True)

        self.NormalSettingWindow.addWidget(self.checkBox_7)

        self.checkBox_11 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setStyleSheet(u"background: none;")
        self.checkBox_11.setChecked(False)

        self.NormalSettingWindow.addWidget(self.checkBox_11)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setStyleSheet(u"background: none;")
        self.checkBox_5.setChecked(True)

        self.NormalSettingWindow.addWidget(self.checkBox_5)

        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.checkBox_9 = QCheckBox(self.frame_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(20, 10, 221, 20))
        self.checkBox_9.setStyleSheet(u"color: #333333;")
        self.checkBox_9.setChecked(True)
        self.checkBox_10 = QCheckBox(self.frame_3)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(False)
        self.checkBox_10.setGeometry(QRect(20, 40, 221, 20))
        self.checkBox_10.setStyleSheet(u"color: #666666;")
        self.checkBox_10.setCheckable(True)
        self.checkBox_10.setChecked(False)
        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 70, 51, 20))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.frame_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(60, 70, 51, 20))
        self.radioButton_2.setChecked(False)
        self.radioButton_3 = QRadioButton(self.frame_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QRect(100, 70, 51, 20))
        self.radioButton_3.setChecked(False)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 10, 61, 22))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setClearButtonEnabled(True)

        self.NormalSettingWindow.addWidget(self.frame_3)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(250, 310, 429, 38))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 10, 61, 22))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 101, 16))
        self.TextEditWindow = QFrame(Form)
        self.TextEditWindow.setObjectName(u"TextEditWindow")
        self.TextEditWindow.setGeometry(QRect(250, 80, 440, 264))
        self.TextEditWindow.setFrameShape(QFrame.Shape.StyledPanel)
        self.TextEditWindow.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.TextEditWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 10, 150, 20))
        self.lineEdit_3 = QLineEdit(self.TextEditWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 10, 190, 20))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.label_10 = QLabel(self.TextEditWindow)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 40, 150, 20))
        self.lineEdit_4 = QLineEdit(self.TextEditWindow)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 40, 190, 20))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_4.setDragEnabled(True)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.label_11 = QLabel(self.TextEditWindow)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 70, 150, 20))
        self.lineEdit_6 = QLineEdit(self.TextEditWindow)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(120, 70, 190, 20))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_6.setDragEnabled(True)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.label_12 = QLabel(self.TextEditWindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 100, 150, 20))
        self.lineEdit_7 = QLineEdit(self.TextEditWindow)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(120, 100, 190, 20))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_7.setDragEnabled(True)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.label_13 = QLabel(self.TextEditWindow)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 130, 150, 20))
        self.lineEdit_8 = QLineEdit(self.TextEditWindow)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(120, 130, 190, 20))
        self.lineEdit_8.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_8.setDragEnabled(True)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.label_14 = QLabel(self.TextEditWindow)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 160, 150, 20))
        self.lineEdit_9 = QLineEdit(self.TextEditWindow)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(120, 160, 190, 20))
        self.lineEdit_9.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_9.setDragEnabled(True)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.label_15 = QLabel(self.TextEditWindow)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 190, 150, 20))
        self.lineEdit_10 = QLineEdit(self.TextEditWindow)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(120, 190, 190, 20))
        self.lineEdit_10.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.lineEdit_10.setDragEnabled(True)
        self.lineEdit_10.setClearButtonEnabled(True)
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(110, 80, 451, 261))
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 220);\n"
"border: 1px solid #DDDDDD;\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 60, 211, 31))
        self.checkBox.setStyleSheet(u"background: none;\n"
"border: none;\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(\"assets/unchecked.png\");	\n"
"	background: none;\n"
"	border: none;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\"assets/checked.png\");\n"
"	background: none;\n"
"	border: none;\n"
"}")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 40, 431, 21))
        self.label_16.setStyleSheet(u"background: none;\n"
"border: none;")
        self.label_16.setFrameShape(QFrame.Shape.HLine)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 281, 31))
        self.label_17.setStyleSheet(u"background: none;\n"
"border: none;")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 140, 281, 31))
        self.label_18.setStyleSheet(u"background: none;\n"
"border: none;")
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 180, 431, 71))
        self.label_19.setStyleSheet(u"background: none;\n"
"border: none;")
        self.TextSetting_2 = QPushButton(self.frame_5)
        self.TextSetting_2.setObjectName(u"TextSetting_2")
        self.TextSetting_2.setGeometry(QRect(410, 10, 31, 31))
        self.TextSetting_2.setStyleSheet(u"background: none;\n"
"border: none;")
        icon6 = QIcon()
        icon6.addFile(u"assets/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TextSetting_2.setIcon(icon6)
        self.TextSetting_2.setIconSize(QSize(24, 24))
        self.TextSetting_2.setCheckable(True)
        self.TextSetting_2.setAutoExclusive(True)
        self.TextSetting_2.setFlat(False)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 90, 111, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: #00CA72;\n"
"	color: #FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00BF6C;\n"
"	color: #FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #007B45;\n"
"	color: #FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"assets/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(24, 24))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 60, 690, 16))
        self.label_9.setPixmap(QPixmap(u"assets/bar.png"))
        self.label_9.setScaledContents(True)
        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(220, 80, 231, 261))
        self.frame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 220);\n"
"border: 1px solid #DDDDDD;\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 10, 281, 31))
        self.label_21.setStyleSheet(u"background: none;\n"
"border: none;")
        self.TextSetting_3 = QPushButton(self.frame_6)
        self.TextSetting_3.setObjectName(u"TextSetting_3")
        self.TextSetting_3.setGeometry(QRect(200, 10, 31, 31))
        self.TextSetting_3.setStyleSheet(u"background: none;\n"
"border: none;")
        self.TextSetting_3.setIcon(icon6)
        self.TextSetting_3.setIconSize(QSize(24, 24))
        self.TextSetting_3.setCheckable(True)
        self.TextSetting_3.setAutoExclusive(True)
        self.TextSetting_3.setFlat(False)
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 40, 211, 61))
        self.label_20.setStyleSheet(u"background: none;\n"
"border: none;")
        self.label_20.setFrameShape(QFrame.Shape.HLine)
        self.label_20.setScaledContents(False)
        self.label_20.setWordWrap(True)
        self.verticalLayoutWidget_2 = QWidget(self.frame_6)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 100, 81, 158))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.timeEdit = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit.setProperty(u"showGroupSeparator", False)
        self.timeEdit.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit)

        self.timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_2.setWrapping(False)
        self.timeEdit_2.setFrame(True)
        self.timeEdit_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_2.setProperty(u"showGroupSeparator", False)
        self.timeEdit_2.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit_2)

        self.timeEdit_3 = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_3.setWrapping(False)
        self.timeEdit_3.setFrame(True)
        self.timeEdit_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_3.setProperty(u"showGroupSeparator", False)
        self.timeEdit_3.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit_3)

        self.timeEdit_4 = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit_4.setObjectName(u"timeEdit_4")
        self.timeEdit_4.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_4.setWrapping(False)
        self.timeEdit_4.setFrame(True)
        self.timeEdit_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_4.setProperty(u"showGroupSeparator", False)
        self.timeEdit_4.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit_4)

        self.timeEdit_5 = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit_5.setObjectName(u"timeEdit_5")
        self.timeEdit_5.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_5.setWrapping(False)
        self.timeEdit_5.setFrame(True)
        self.timeEdit_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_5.setProperty(u"showGroupSeparator", False)
        self.timeEdit_5.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit_5)

        self.timeEdit_6 = QTimeEdit(self.verticalLayoutWidget_2)
        self.timeEdit_6.setObjectName(u"timeEdit_6")
        self.timeEdit_6.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_6.setWrapping(False)
        self.timeEdit_6.setFrame(True)
        self.timeEdit_6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_6.setProperty(u"showGroupSeparator", False)
        self.timeEdit_6.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.timeEdit_6)

        self.verticalLayoutWidget_3 = QWidget(self.frame_6)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(120, 100, 81, 158))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.timeEdit_7 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_7.setObjectName(u"timeEdit_7")
        self.timeEdit_7.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_7.setWrapping(False)
        self.timeEdit_7.setFrame(True)
        self.timeEdit_7.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_7.setProperty(u"showGroupSeparator", False)
        self.timeEdit_7.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_7)

        self.timeEdit_8 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_8.setObjectName(u"timeEdit_8")
        self.timeEdit_8.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_8.setWrapping(False)
        self.timeEdit_8.setFrame(True)
        self.timeEdit_8.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_8.setProperty(u"showGroupSeparator", False)
        self.timeEdit_8.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_8)

        self.timeEdit_9 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_9.setObjectName(u"timeEdit_9")
        self.timeEdit_9.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_9.setWrapping(False)
        self.timeEdit_9.setFrame(True)
        self.timeEdit_9.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_9.setProperty(u"showGroupSeparator", False)
        self.timeEdit_9.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_9)

        self.timeEdit_10 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_10.setObjectName(u"timeEdit_10")
        self.timeEdit_10.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_10.setWrapping(False)
        self.timeEdit_10.setFrame(True)
        self.timeEdit_10.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_10.setProperty(u"showGroupSeparator", False)
        self.timeEdit_10.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_10)

        self.timeEdit_11 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_11.setObjectName(u"timeEdit_11")
        self.timeEdit_11.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_11.setWrapping(False)
        self.timeEdit_11.setFrame(True)
        self.timeEdit_11.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_11.setProperty(u"showGroupSeparator", False)
        self.timeEdit_11.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_11)

        self.timeEdit_12 = QTimeEdit(self.verticalLayoutWidget_3)
        self.timeEdit_12.setObjectName(u"timeEdit_12")
        self.timeEdit_12.setStyleSheet(u"QtimeEdit{\n"
"	border: 1px solid #DDDDDD;\n"
"	border-radius: 5px;\n"
"}\n"
"QtimeEdit:hover{\n"
"	border: 1px solid #4DD4A6;\n"
"	border-radius: 5px;\n"
"}")
        self.timeEdit_12.setWrapping(False)
        self.timeEdit_12.setFrame(True)
        self.timeEdit_12.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEdit_12.setProperty(u"showGroupSeparator", False)
        self.timeEdit_12.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.timeEdit_12)

        self.toast = QFrame(Form)
        self.toast.setObjectName(u"toast")
        self.toast.setGeometry(QRect(230, 49, 211, 41))
        self.toast.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: #FFFFFF;\n"
"border-radius: 20px;")
        self.toast.setFrameShape(QFrame.Shape.StyledPanel)
        self.toast.setFrameShadow(QFrame.Shadow.Raised)
        self.label_22 = QLabel(self.toast)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 24, 24))
        self.label_22.setStyleSheet(u"background:none;")
        self.label_22.setPixmap(QPixmap(u"assets/saveok.png"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.toast)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 10, 151, 21))
        self.label_23.setStyleSheet(u"background: none;")
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.frame_4.raise_()
        self.TextEditWindow.raise_()
        self.label_9.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.toast.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"360\u62d6\u5802\u536b\u58eb", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4e3a\u60a8\u7684\u8bfe\u5802\u4fdd\u9a7e\u62a4\u822a</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">360\u62d6\u5802\u536b\u58eb</span></p></body></html>", None))
        self.label_6.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.Setting.setText("")
        self.TextSetting.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u82e5\u8ba9ClassIsland\u7b49\u65f6\u95f4\u8868\u7a0b\u5e8f\u63a5\u7ba1\u4e0b\u8bfe\u4e8b\u4ef6\uff0c\u4e0b\u8bfe\u65f6\u95f4\u7f16\u8f91\u5668\u5c06\u4e0d\u518d\u53ef\u7528&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\u65f6\u95f4\u8868\u89e6\u53d1\u5468\u671f\uff1a60s</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">\u62d6\u5802\u9632\u62a4\u5df2\u5f00\u542f</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u8981\u67e5\u6740\u7684\u7a0b\u5e8f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u4e0b\u8bfe/\u7528\u9910\u65f6\u95f4", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u6027\u9009\u9879/\u5173\u4e8e", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u67e5\u6740PowerPoint", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u67e5\u6740\u5e0c\u6c83\u767d\u677f", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u67e5\u6740\u5e0c\u6c83\u5c55\u53f0", None))
        self.checkBox_11.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u67e5\u6740\u6307\u5b9a\u7684\u7a0b\u5e8f", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"\u6ee1\u8db3\u4e0b\u5217\u6761\u4ef6\u65f6\u6267\u884c\u5f3a\u5236\u63aa\u65bd", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"\u62d6\u5802\u8d85\u8fc7\u79d2\u6570", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u540e\u662f\u7528\u9910\u65f6\u95f4\uff08\u656c\u8bf7\u671f\u5f85\uff09", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u4e0e", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6216", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u975e", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"300", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u65e0\u4eba\u503c\u5b88\u5012\u8ba1\u65f6</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7a97\u53e3\u6807\u9898\u6587\u672c", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u63d0\u9192\u6587\u672c", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u62d6\u5802\u9009\u9879\u6587\u672c", None))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u9009\u9879\u6587\u672c", None))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u4fe1\u606f\u6846\u6807\u9898\u6587\u672c", None))
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u62d6\u5802\u4fe1\u606f", None))
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u4fe1\u606f", None))
        self.lineEdit_10.setInputMask("")
        self.lineEdit_10.setText(QCoreApplication.translate("Form", u"30", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u8ba9ClassIsland\u63a5\u7ba1\u4e0b\u8bfe\u4e8b\u4ef6", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700; color:#ff0000;\">\u5371\u9669\uff01\u9664\u975e\u60a8\u660e\u786e\u4e0b\u65b9\u5404\u4e2a\u9009\u9879\u7684\u7528\u9014\u548c\u540e\u679c\uff0c\u5426\u5219\u4e0d\u8981\u4fee\u6539\u4efb\u610f\u5185\u5bb9\uff01</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Pandora Boxxx</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u5173\u4e8e</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">\u7a0b\u5e8f\u4f5c\u8005\uff1axxt8582753</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">\u7f51\u7ad9\uff1a</span><a href=\"https://xxtsoft.top\"><span style=\" text-decoration: underline; color:#0000ff;\">https://xxtsoft.top</span></a></p>\n"
"<p st"
                        "yle=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">\u90ae\u7bb1\uff1a</span><a href=\"mailto:xxt8582753@126.com\"><span style=\" text-decoration: underline; color:#0000ff;\">xxt8582753@126.com</span></a></p></body></html>", None))
        self.TextSetting_2.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91JSON", None))
        self.label_9.setText("")
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u4e0b\u8bfe\u65f6\u95f4\u7f16\u8f91\u5668</span></p></body></html>", None))
        self.TextSetting_3.setText("")
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8f93\u516524\u5c0f\u65f6\u5236\u4e0b\u8bfe\u65f6\u95f4\uff0c\u9ed8\u8ba400:00:00\u7559\u7a7a\uff08\u5e94\u8be5\u6ca1\u6709\u5b66\u6821\u8fd9\u4e2a\u70b9\u4e0b\u8bfe\u5427\uff09</p><p>\u63d0\u793a\uff1a\u53ef\u4ee5\u6309Tab\u5207\u6362\u7126\u70b9</p></body></html>", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_3.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_4.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_5.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_6.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_7.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_8.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_9.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_10.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_11.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.timeEdit_12.setDisplayFormat(QCoreApplication.translate("Form", u"HH:mm:ss", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u4fdd\u5b58\u6210\u529f\uff0c\u91cd\u542f\u540e\u751f\u6548", None))
    # retranslateUi

