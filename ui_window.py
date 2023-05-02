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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLayout, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
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
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 470, 271, 41))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.browseBtn = QPushButton(self.formLayoutWidget)
        self.browseBtn.setObjectName(u"browseBtn")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.browseBtn)

        self.browseTxt = QTextEdit(self.formLayoutWidget)
        self.browseTxt.setObjectName(u"browseTxt")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.browseTxt)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 340, 271, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.eulaBtn = QRadioButton(self.centralwidget)
        self.eulaBtn.setObjectName(u"eulaBtn")
        self.eulaBtn.setGeometry(QRect(0, 0, 105, 22))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 520, 401, 20))
        self.progressBar.setValue(24)
        self.createBtn = QPushButton(self.centralwidget)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setGeometry(QRect(280, 470, 121, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft Server Maker", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.eulaBtn.setText(QCoreApplication.translate("MainWindow", u"Accept eula", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

