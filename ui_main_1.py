# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_1tDktrK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 456)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.011, x2:0.972, y2:0.965909, stop:0.113636 rgba(26, 23, 59, 255), stop:1 rgba(63, 37, 63, 255));\n"
"border-radius: 10px;\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color: rgba(85, 85, 127, 20);\n"
"border-bottom:1px solid rgb(122, 104, 136);\n"
"border-radius:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.frame_titles = QFrame(self.title_bar)
        self.frame_titles.setObjectName(u"frame_titles")
        self.frame_titles.setStyleSheet(u"border-bottom:none;\n"
"border-radius:none;")
        self.frame_titles.setFrameShape(QFrame.NoFrame)
        self.frame_titles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_titles)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_11 = QLabel(self.frame_titles)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_titles)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(70, 0))
        self.frame_btns.setMaximumSize(QSize(90, 16777215))
        self.frame_btns.setStyleSheet(u"border-bottom:none;\n"
"border-radius:none;")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(14, 14))
        self.btn_maximize.setMaximumSize(QSize(14, 14))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(14, 14))
        self.btn_minimize.setMaximumSize(QSize(14, 14))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(14, 14))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 84, 5);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;\n"
"border-top: none;\n"
"\n"
"")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tools = QFrame(self.content_bar)
        self.tools.setObjectName(u"tools")
        self.tools.setMinimumSize(QSize(50, 0))
        self.tools.setMaximumSize(QSize(50, 16777215))
        self.tools.setStyleSheet(u"border-radius: 0px;\n"
"background-color: rgb(26, 23, 59);\n"
"border-right:1px solid rgb(122, 104, 136);\n"
"")
        self.tools.setFrameShape(QFrame.StyledPanel)
        self.tools.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.tools, 0, 0, 2, 1)

        self.frame = QFrame(self.content_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-top:1px solid rgb(122, 104, 136);\n"
"border-radius:0px;\n"
"")
        self.gridLayout_26 = QGridLayout(self.frame)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(15)
        self.gridLayout_26.setVerticalSpacing(6)
        self.gridLayout_26.setContentsMargins(10, 0, 20, 15)
        self.rd_new = QRadioButton(self.frame)
        self.rd_new.setObjectName(u"rd_new")
        self.rd_new.setMinimumSize(QSize(23, 20))
        self.rd_new.setMaximumSize(QSize(90, 16777215))
        self.rd_new.setFocusPolicy(Qt.ClickFocus)
        self.rd_new.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(211, 211, 211);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border-bottom: none;\n"
"	background-color: none;\n"
"	alternate-background-color: rgb(255, 170, 255);	\n"
"	border-radius: 0px;\n"
"	border-top:0px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	border-radius:6px;\n"
"	width: 9px;\n"
"	height: 9px;\n"
"	background-color: rgb(36, 34, 58);\n"
"	border: 2px solid rgb(202, 202, 202);\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	border-radius: 6px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}")

        self.gridLayout_26.addWidget(self.rd_new, 2, 0, 1, 1)

        self.bt_load = QPushButton(self.frame)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setMinimumSize(QSize(80, 30))
        self.bt_load.setMaximumSize(QSize(70000, 23))
        self.bt_load.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")

        self.gridLayout_26.addWidget(self.bt_load, 3, 2, 1, 2)

        self.label_42 = QLabel(self.frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;\n"
"border-top:0px;\n"
"border-radius:0px;\n"
"")

        self.gridLayout_26.addWidget(self.label_42, 1, 2, 1, 2)

        self.rd_csv = QRadioButton(self.frame)
        self.rd_csv.setObjectName(u"rd_csv")
        self.rd_csv.setMinimumSize(QSize(60, 20))
        self.rd_csv.setMaximumSize(QSize(60, 16777215))
        self.rd_csv.setFocusPolicy(Qt.ClickFocus)
        self.rd_csv.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(211, 211, 211);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border-bottom: none;\n"
"	background-color: none;\n"
"	alternate-background-color: rgb(255, 170, 255);	\n"
"	border-radius: 0px;\n"
"	border-top:0px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	border-radius:6px;\n"
"	width: 9px;\n"
"	height: 9px;\n"
"	background-color: rgb(36, 34, 58);\n"
"	border: 2px solid rgb(202, 202, 202);\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	border-radius: 6px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}")

        self.gridLayout_26.addWidget(self.rd_csv, 2, 2, 1, 1)

        self.le_local = QLineEdit(self.frame)
        self.le_local.setObjectName(u"le_local")
        self.le_local.setMinimumSize(QSize(0, 30))
        self.le_local.setMaximumSize(QSize(5000, 23))
        self.le_local.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius: 15px;\n"
"	padding: 25px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")

        self.gridLayout_26.addWidget(self.le_local, 3, 1, 1, 1)

        self.rd_excel = QRadioButton(self.frame)
        self.rd_excel.setObjectName(u"rd_excel")
        self.rd_excel.setMinimumSize(QSize(60, 20))
        self.rd_excel.setMaximumSize(QSize(60, 16777215))
        self.rd_excel.setFocusPolicy(Qt.ClickFocus)
        self.rd_excel.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(211, 211, 211);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border-bottom: none;\n"
"	background-color: none;\n"
"	alternate-background-color: rgb(255, 170, 255);	\n"
"	border-radius: 0px;\n"
"	border-top:0px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	border-radius:6px;\n"
"	width: 9px;\n"
"	height: 9px;\n"
"	background-color: rgb(36, 34, 58);\n"
"	border: 2px solid rgb(202, 202, 202);\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	border-radius: 6px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}")

        self.gridLayout_26.addWidget(self.rd_excel, 2, 3, 1, 1)

        self.rd_existing = QRadioButton(self.frame)
        self.rd_existing.setObjectName(u"rd_existing")
        self.rd_existing.setMinimumSize(QSize(40, 20))
        self.rd_existing.setMaximumSize(QSize(65, 16777215))
        self.rd_existing.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(211, 211, 211);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border-bottom: none;\n"
"	background-color: none;\n"
"	alternate-background-color: rgb(255, 170, 255);	\n"
"	border-radius: 0px;\n"
"	border-top:0px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	border-radius:6px;\n"
"	width: 9px;\n"
"	height: 9px;\n"
"	background-color: rgb(36, 34, 58);\n"
"	border: 2px solid rgb(202, 202, 202);\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	border-radius: 6px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}")

        self.gridLayout_26.addWidget(self.rd_existing, 3, 0, 1, 1)

        self.label_58 = QLabel(self.frame)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 30))
        self.label_58.setMaximumSize(QSize(16777215, 23))
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;\n"
"border-top:0px;\n"
"border-radius:0px;\n"
"")

        self.gridLayout_26.addWidget(self.label_58, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)

        self.frame1 = QFrame(self.content_bar)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 239))
        self.gridLayout_2 = QGridLayout(self.frame1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(10)
        self.gridLayout_27.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_29 = QSpacerItem(127, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_29, 0, 0, 1, 1)

        self.bt_return = QPushButton(self.frame1)
        self.bt_return.setObjectName(u"bt_return")
        self.bt_return.setMinimumSize(QSize(100, 20))
        self.bt_return.setMaximumSize(QSize(150, 23))
        self.bt_return.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")

        self.gridLayout_27.addWidget(self.bt_return, 0, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(127, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_30, 0, 3, 1, 1)

        self.bt_forward = QPushButton(self.frame1)
        self.bt_forward.setObjectName(u"bt_forward")
        self.bt_forward.setMinimumSize(QSize(100, 20))
        self.bt_forward.setMaximumSize(QSize(150, 23))
        self.bt_forward.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")

        self.gridLayout_27.addWidget(self.bt_forward, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_27, 1, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.frame1)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 90))
        self.stackedWidget.setStyleSheet(u"border-radius: 0px;\n"
"background-color:none;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_29 = QGridLayout(self.page)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.page)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 0))
        self.frame_54.setMaximumSize(QSize(16777215, 7))
        self.frame_54.setLayoutDirection(Qt.LeftToRight)
        self.frame_54.setStyleSheet(u"background-color: none;")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_32 = QSpacerItem(267, 4, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_32)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(4)
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(20, 5))
        self.frame_55.setMaximumSize(QSize(20, 5))
        self.frame_55.setStyleSheet(u"background-color:  rgb(67, 230, 255);")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)

        self.gridLayout_31.addWidget(self.frame_55, 0, 0, 1, 1)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(20, 5))
        self.frame_56.setMaximumSize(QSize(20, 5))
        self.frame_56.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.gridLayout_31.addWidget(self.frame_56, 0, 1, 1, 1)

        self.frame_57 = QFrame(self.frame_54)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(20, 5))
        self.frame_57.setMaximumSize(QSize(20, 5))
        self.frame_57.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)

        self.gridLayout_31.addWidget(self.frame_57, 0, 2, 1, 1)

        self.frame_58 = QFrame(self.frame_54)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(20, 5))
        self.frame_58.setMaximumSize(QSize(20, 5))
        self.frame_58.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.gridLayout_31.addWidget(self.frame_58, 0, 3, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_31)

        self.horizontalSpacer_33 = QSpacerItem(267, 4, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_33)


        self.gridLayout_29.addWidget(self.frame_54, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 0, 0, 20)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.sb_qtn_tables = QSpinBox(self.page)
        self.sb_qtn_tables.setObjectName(u"sb_qtn_tables")
        self.sb_qtn_tables.setMinimumSize(QSize(60, 25))
        self.sb_qtn_tables.setMaximumSize(QSize(80, 16777215))
        self.sb_qtn_tables.setStyleSheet(u"QSpinBox {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius:10px;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	background-color: rgb(66, 61, 106);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"	background-color: rgb(71, 51, 93);\n"
"	border:1px solid rgb(122, 104, 136);\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"QSpinBox::down-button{\n"
"	background-color: rgb(71, 51, 93);\n"
"	border:1px solid rgb(122, 104, 136);\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.sb_qtn_tables.setMinimum(2)
        self.sb_qtn_tables.setMaximum(4)

        self.gridLayout.addWidget(self.sb_qtn_tables, 1, 1, 1, 3)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 5)

        self.label_44 = QLabel(self.page)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 30))
        self.label_44.setMaximumSize(QSize(16777215, 30))
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_44, 4, 0, 1, 5)

        self.le_file1 = QLineEdit(self.page)
        self.le_file1.setObjectName(u"le_file1")
        self.le_file1.setMinimumSize(QSize(300, 30))
        self.le_file1.setMaximumSize(QSize(500, 30))
        self.le_file1.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius: 15px;\n"
"	padding: 25px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.le_file1, 3, 1, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.le_file2 = QLineEdit(self.page)
        self.le_file2.setObjectName(u"le_file2")
        self.le_file2.setMinimumSize(QSize(350, 30))
        self.le_file2.setMaximumSize(QSize(500, 30))
        self.le_file2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius: 15px;\n"
"	padding: 25px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.le_file2, 5, 1, 1, 4)

        self.label_45 = QLabel(self.page)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 30))
        self.label_45.setMaximumSize(QSize(16777215, 23))
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_45, 0, 0, 1, 5)


        self.gridLayout_29.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_19 = QVBoxLayout(self.page_10)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(20)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(20, 0, 20, 20)
        self.label_49 = QLabel(self.page_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 30))
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_49, 0, 1, 1, 1)

        self.label_48 = QLabel(self.page_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 30))
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_48, 0, 2, 1, 1)

        self.label_46 = QLabel(self.page_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 30))
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_46, 2, 1, 1, 1)

        self.label_47 = QLabel(self.page_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 30))
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_47, 0, 0, 1, 1)

        self.cb_column1 = QComboBox(self.page_10)
        self.cb_column1.setObjectName(u"cb_column1")
        self.cb_column1.setMinimumSize(QSize(0, 23))
        self.cb_column1.setMaximumSize(QSize(16777215, 23))
        self.cb_column1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_column1, 1, 1, 1, 1)

        self.label_50 = QLabel(self.page_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 30))
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_50, 2, 0, 1, 1)

        self.cb_column2 = QComboBox(self.page_10)
        self.cb_column2.setObjectName(u"cb_column2")
        self.cb_column2.setMinimumSize(QSize(0, 23))
        self.cb_column2.setMaximumSize(QSize(16777215, 23))
        self.cb_column2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_column2, 3, 1, 1, 1)

        self.cb_relationship1 = QComboBox(self.page_10)
        self.cb_relationship1.setObjectName(u"cb_relationship1")
        self.cb_relationship1.setMinimumSize(QSize(0, 23))
        self.cb_relationship1.setMaximumSize(QSize(100, 23))
        self.cb_relationship1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_relationship1, 1, 2, 1, 1)

        self.cb_sheets1 = QComboBox(self.page_10)
        self.cb_sheets1.setObjectName(u"cb_sheets1")
        self.cb_sheets1.setMinimumSize(QSize(0, 23))
        self.cb_sheets1.setMaximumSize(QSize(16777215, 23))
        self.cb_sheets1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_sheets1, 1, 0, 1, 1)

        self.cb_sheets2 = QComboBox(self.page_10)
        self.cb_sheets2.setObjectName(u"cb_sheets2")
        self.cb_sheets2.setMinimumSize(QSize(0, 23))
        self.cb_sheets2.setMaximumSize(QSize(16777215, 23))
        self.cb_sheets2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_sheets2, 3, 0, 1, 1)

        self.cb_select_columns = QComboBox(self.page_10)
        self.cb_select_columns.setObjectName(u"cb_select_columns")
        self.cb_select_columns.setMinimumSize(QSize(0, 23))
        self.cb_select_columns.setMaximumSize(QSize(100, 23))
        self.cb_select_columns.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_32.addWidget(self.cb_select_columns, 3, 2, 1, 1)

        self.label_59 = QLabel(self.page_10)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 30))
        self.label_59.setFont(font)
        self.label_59.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_32.addWidget(self.label_59, 2, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_32)

        self.frame_59 = QFrame(self.page_10)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 0))
        self.frame_59.setMaximumSize(QSize(16777215, 7))
        self.frame_59.setLayoutDirection(Qt.LeftToRight)
        self.frame_59.setStyleSheet(u"background-color: none;")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_34)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(4)
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(20, 5))
        self.frame_60.setMaximumSize(QSize(20, 5))
        self.frame_60.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.gridLayout_33.addWidget(self.frame_60, 0, 0, 1, 1)

        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(20, 5))
        self.frame_61.setMaximumSize(QSize(20, 5))
        self.frame_61.setStyleSheet(u"background-color:  rgb(67, 230, 255);\n"
"border-radius: 5px;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.gridLayout_33.addWidget(self.frame_61, 0, 1, 1, 1)

        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(20, 5))
        self.frame_62.setMaximumSize(QSize(20, 5))
        self.frame_62.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.gridLayout_33.addWidget(self.frame_62, 0, 2, 1, 1)

        self.frame_63 = QFrame(self.frame_59)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(20, 5))
        self.frame_63.setMaximumSize(QSize(20, 5))
        self.frame_63.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.gridLayout_33.addWidget(self.frame_63, 0, 3, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_33)

        self.horizontalSpacer_35 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_35)


        self.verticalLayout_19.addWidget(self.frame_59)

        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_20 = QVBoxLayout(self.page_11)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(20, 20, 20, 20)
        self.lineEdit_14 = QLineEdit(self.page_11)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(350, 30))
        self.lineEdit_14.setMaximumSize(QSize(16777215, 23))
        self.lineEdit_14.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 15px;\n"
"	padding: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")

        self.gridLayout_34.addWidget(self.lineEdit_14, 3, 1, 1, 2)

        self.horizontalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_36, 1, 0, 1, 1)

        self.label_51 = QLabel(self.page_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_34.addWidget(self.label_51, 0, 0, 1, 3)

        self.lineEdit_15 = QLineEdit(self.page_11)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(350, 30))
        self.lineEdit_15.setMaximumSize(QSize(16777215, 23))
        self.lineEdit_15.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 15px;\n"
"	padding: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")

        self.gridLayout_34.addWidget(self.lineEdit_15, 1, 1, 1, 2)

        self.label_52 = QLabel(self.page_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)
        self.label_52.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_34.addWidget(self.label_52, 2, 0, 1, 3)


        self.verticalLayout_20.addLayout(self.gridLayout_34)

        self.frame_64 = QFrame(self.page_11)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 0))
        self.frame_64.setMaximumSize(QSize(16777215, 7))
        self.frame_64.setLayoutDirection(Qt.LeftToRight)
        self.frame_64.setStyleSheet(u"background-color: none;")
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_37 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_37)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setHorizontalSpacing(4)
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(20, 5))
        self.frame_65.setMaximumSize(QSize(20, 5))
        self.frame_65.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.gridLayout_35.addWidget(self.frame_65, 0, 0, 1, 1)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(20, 5))
        self.frame_66.setMaximumSize(QSize(20, 5))
        self.frame_66.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.gridLayout_35.addWidget(self.frame_66, 0, 1, 1, 1)

        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(20, 5))
        self.frame_67.setMaximumSize(QSize(20, 5))
        self.frame_67.setStyleSheet(u"background-color: rgb(67, 230, 255);\n"
"border-radius: 5px;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.gridLayout_35.addWidget(self.frame_67, 0, 2, 1, 1)

        self.frame_68 = QFrame(self.frame_64)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(20, 5))
        self.frame_68.setMaximumSize(QSize(20, 5))
        self.frame_68.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.gridLayout_35.addWidget(self.frame_68, 0, 3, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_35)

        self.horizontalSpacer_38 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_38)


        self.verticalLayout_20.addWidget(self.frame_64)

        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_21 = QVBoxLayout(self.page_12)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setHorizontalSpacing(20)
        self.gridLayout_36.setVerticalSpacing(10)
        self.gridLayout_36.setContentsMargins(15, 50, 15, 50)
        self.comboBox_16 = QComboBox(self.page_12)
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setMinimumSize(QSize(0, 23))
        self.comboBox_16.setMaximumSize(QSize(16777215, 23))
        self.comboBox_16.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_36.addWidget(self.comboBox_16, 3, 1, 1, 1)

        self.comboBox_17 = QComboBox(self.page_12)
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMinimumSize(QSize(0, 23))
        self.comboBox_17.setMaximumSize(QSize(16777215, 23))
        self.comboBox_17.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_36.addWidget(self.comboBox_17, 1, 0, 1, 1)

        self.comboBox_18 = QComboBox(self.page_12)
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMinimumSize(QSize(0, 23))
        self.comboBox_18.setMaximumSize(QSize(16777215, 23))
        self.comboBox_18.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_36.addWidget(self.comboBox_18, 1, 1, 1, 1)

        self.label_53 = QLabel(self.page_12)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)
        self.label_53.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_36.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_54 = QLabel(self.page_12)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_36.addWidget(self.label_54, 2, 1, 1, 1)

        self.comboBox_19 = QComboBox(self.page_12)
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(0, 23))
        self.comboBox_19.setMaximumSize(QSize(16777215, 23))
        self.comboBox_19.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_36.addWidget(self.comboBox_19, 3, 0, 1, 1)

        self.comboBox_20 = QComboBox(self.page_12)
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMinimumSize(QSize(0, 23))
        self.comboBox_20.setMaximumSize(QSize(100, 23))
        self.comboBox_20.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(59, 54, 94);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid rgb(35, 33, 57);\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout_36.addWidget(self.comboBox_20, 2, 2, 1, 1)

        self.label_55 = QLabel(self.page_12)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_36.addWidget(self.label_55, 1, 2, 1, 1)

        self.label_56 = QLabel(self.page_12)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)
        self.label_56.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_36.addWidget(self.label_56, 2, 0, 1, 1)

        self.label_57 = QLabel(self.page_12)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.gridLayout_36.addWidget(self.label_57, 0, 1, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_36)

        self.frame_69 = QFrame(self.page_12)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 0))
        self.frame_69.setMaximumSize(QSize(16777215, 7))
        self.frame_69.setLayoutDirection(Qt.LeftToRight)
        self.frame_69.setStyleSheet(u"background-color: none;")
        self.frame_69.setFrameShape(QFrame.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_39 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_39)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setHorizontalSpacing(4)
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(20, 5))
        self.frame_70.setMaximumSize(QSize(20, 5))
        self.frame_70.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.gridLayout_37.addWidget(self.frame_70, 0, 0, 1, 1)

        self.frame_71 = QFrame(self.frame_69)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(20, 5))
        self.frame_71.setMaximumSize(QSize(20, 5))
        self.frame_71.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.gridLayout_37.addWidget(self.frame_71, 0, 1, 1, 1)

        self.frame_72 = QFrame(self.frame_69)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(20, 5))
        self.frame_72.setMaximumSize(QSize(20, 5))
        self.frame_72.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"border-radius: 5px;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.gridLayout_37.addWidget(self.frame_72, 0, 2, 1, 1)

        self.frame_73 = QFrame(self.frame_69)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(20, 5))
        self.frame_73.setMaximumSize(QSize(20, 5))
        self.frame_73.setStyleSheet(u"background-color:  rgb(67, 230, 255);")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.gridLayout_37.addWidget(self.frame_73, 0, 3, 1, 1)


        self.horizontalLayout_15.addLayout(self.gridLayout_37)

        self.horizontalSpacer_40 = QSpacerItem(281, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)


        self.verticalLayout_21.addWidget(self.frame_69)

        self.stackedWidget.addWidget(self.page_12)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame1, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.horizontalLayout_3.addWidget(self.content_bar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(17, 15, 38);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"\n"
"border-top:1px solid rgb(122, 104, 136);\n"
"")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.credits_bar)

        self.credits_bar.raise_()
        self.title_bar.raise_()

        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#7ac8f8;\">SciApp</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.rd_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Type:</p></body></html>", None))
        self.rd_csv.setText(QCoreApplication.translate("MainWindow", u".CSV", None))
#if QT_CONFIG(tooltip)
        self.le_local.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.le_local.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/DataSci/Documents/name.xlsx", None))
        self.rd_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.rd_existing.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>File to save:</p></body></html>", None))
        self.bt_return.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.bt_forward.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>First table:</p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Second table:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.le_file1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.le_file1.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.le_file1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/DataSci/Documents/name.xlsx", None))
#if QT_CONFIG(tooltip)
        self.le_file2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.le_file2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.le_file2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/DataSci/Documents/name.xlsx", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Tables to merge:</p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose first column to merge:</p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Type relationship:</p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Choose second column to merge:</p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select first worksheet:</p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select second worksheet:</p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Type relationship:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_14.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/Likely/Documents/nome_arquivo.xlsx", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Onde est\u00e1 o 3\u00ba arquivo?</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_15.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/Likely/Documents/nome_arquivo.xlsx", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Onde est\u00e1 o 4\u00ba arquivo?</p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escolha a planilha do 3\u00ba arquivo:</p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escolha a coluna do 4\u00ba arquivo:</p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escolha a rela\u00e7\u00e3o:</p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escolha a planilha do 4\u00ba arquivo:</p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escolha a planilha do 3\u00ba arquivo:</p></body></html>", None))
    # retranslateUi

