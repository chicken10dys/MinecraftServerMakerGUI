# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLayout, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(400, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 550, 401, 20))
        self.progressBar.setValue(24)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 489, 401, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.browseBtn = QPushButton(self.horizontalLayoutWidget)
        self.browseBtn.setObjectName(u"browseBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.browseBtn)

        self.browseTxt = QTextEdit(self.horizontalLayoutWidget)
        self.browseTxt.setObjectName(u"browseTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(25)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browseTxt.sizePolicy().hasHeightForWidth())
        self.browseTxt.setSizePolicy(sizePolicy1)
        self.browseTxt.setMinimumSize(QSize(0, 25))
        self.browseTxt.setBaseSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.browseTxt)

        self.createBtn = QPushButton(self.horizontalLayoutWidget)
        self.createBtn.setObjectName(u"createBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.createBtn)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 401, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.eulaBtn = QRadioButton(self.formLayoutWidget)
        self.eulaBtn.setObjectName(u"eulaBtn")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.eulaBtn)

        self.mcVersionDrop = QComboBox(self.formLayoutWidget)
        self.mcVersionDrop.setObjectName(u"mcVersionDrop")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mcVersionDrop)

        self.mcVersionTxt = QTextEdit(self.formLayoutWidget)
        self.mcVersionTxt.setObjectName(u"mcVersionTxt")
        self.mcVersionTxt.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.mcVersionTxt)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft Server Maker", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.eulaBtn.setText(QCoreApplication.translate("MainWindow", u"Accept eula", None))
        self.mcVersionTxt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Minecraft version</p></body></html>", None))
    # retranslateUi

