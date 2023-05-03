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
    QLayout, QMainWindow, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 600)
        MainWindow.setMinimumSize(QSize(300, 600))
        MainWindow.setMaximumSize(QSize(300, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 301, 181))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.eulaBtn = QRadioButton(self.formLayoutWidget)
        self.eulaBtn.setObjectName(u"eulaBtn")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.eulaBtn)

        self.mcVersionDrop = QComboBox(self.formLayoutWidget)
        self.mcVersionDrop.setObjectName(u"mcVersionDrop")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mcVersionDrop)

        self.ramDrop = QComboBox(self.formLayoutWidget)
        self.ramDrop.setObjectName(u"ramDrop")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ramDrop)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.formLayout.setLayout(6, QFormLayout.SpanningRole, self.horizontalLayout)

        self.browseBtn = QPushButton(self.formLayoutWidget)
        self.browseBtn.setObjectName(u"browseBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.browseBtn)

        self.browseTxt = QPlainTextEdit(self.formLayoutWidget)
        self.browseTxt.setObjectName(u"browseTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(25)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browseTxt.sizePolicy().hasHeightForWidth())
        self.browseTxt.setSizePolicy(sizePolicy1)
        self.browseTxt.setMinimumSize(QSize(0, 25))
        self.browseTxt.setBaseSize(QSize(0, 25))
        self.browseTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.browseTxt)

        self.mcVersionTxt = QPlainTextEdit(self.formLayoutWidget)
        self.mcVersionTxt.setObjectName(u"mcVersionTxt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mcVersionTxt.sizePolicy().hasHeightForWidth())
        self.mcVersionTxt.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.mcVersionTxt)

        self.ramTxt = QPlainTextEdit(self.formLayoutWidget)
        self.ramTxt.setObjectName(u"ramTxt")
        sizePolicy2.setHeightForWidth(self.ramTxt.sizePolicy().hasHeightForWidth())
        self.ramTxt.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ramTxt)

        self.createBtn = QPushButton(self.centralwidget)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setGeometry(QRect(0, 490, 301, 40))
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy3)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 540, 299, 26))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft Server Maker", None))
        self.eulaBtn.setText(QCoreApplication.translate("MainWindow", u"Accept eula", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.browseTxt.setPlainText("")
        self.browseTxt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Save path", None))
        self.mcVersionTxt.setPlainText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.ramTxt.setPlainText(QCoreApplication.translate("MainWindow", u"Ram:", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

