# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QMainWindow, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 600)
        MainWindow.setMinimumSize(QSize(300, 600))
        MainWindow.setMaximumSize(QSize(300, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.verticalLayout_2)

        self.mcVersionTxt = QPlainTextEdit(self.centralwidget)
        self.mcVersionTxt.setObjectName(u"mcVersionTxt")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mcVersionTxt.sizePolicy().hasHeightForWidth())
        self.mcVersionTxt.setSizePolicy(sizePolicy)
        self.mcVersionTxt.setMaximumSize(QSize(16777215, 40))
        self.mcVersionTxt.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.mcVersionTxt)

        self.mcVersionDrop = QComboBox(self.centralwidget)
        self.mcVersionDrop.setObjectName(u"mcVersionDrop")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mcVersionDrop)

        self.ramTxt = QPlainTextEdit(self.centralwidget)
        self.ramTxt.setObjectName(u"ramTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ramTxt.sizePolicy().hasHeightForWidth())
        self.ramTxt.setSizePolicy(sizePolicy1)
        self.ramTxt.setMaximumSize(QSize(16777215, 40))
        self.ramTxt.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.ramTxt)

        self.ramDrop = QComboBox(self.centralwidget)
        self.ramDrop.setObjectName(u"ramDrop")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ramDrop)

        self.browseTxt = QPlainTextEdit(self.centralwidget)
        self.browseTxt.setObjectName(u"browseTxt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(25)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.browseTxt.sizePolicy().hasHeightForWidth())
        self.browseTxt.setSizePolicy(sizePolicy2)
        self.browseTxt.setMinimumSize(QSize(0, 25))
        self.browseTxt.setMaximumSize(QSize(16777215, 50))
        self.browseTxt.setBaseSize(QSize(0, 25))
        self.browseTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.browseTxt)

        self.browseBtn = QPushButton(self.centralwidget)
        self.browseBtn.setObjectName(u"browseBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy3)
        self.browseBtn.setMaximumSize(QSize(16777215, 50))

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.browseBtn)

        self.crossplayBtn = QCheckBox(self.centralwidget)
        self.crossplayBtn.setObjectName(u"crossplayBtn")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.crossplayBtn)

        self.eulaBtn = QCheckBox(self.centralwidget)
        self.eulaBtn.setObjectName(u"eulaBtn")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.eulaBtn)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)

        self.createBtn = QPushButton(self.centralwidget)
        self.createBtn.setObjectName(u"createBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy4)
        self.createBtn.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.createBtn, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 32))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft Server Maker", None))
        self.mcVersionTxt.setPlainText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.ramTxt.setPlainText(QCoreApplication.translate("MainWindow", u"Ram:", None))
        self.browseTxt.setPlainText("")
        self.browseTxt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Save path", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.crossplayBtn.setText(QCoreApplication.translate("MainWindow", u"Java bedrock crossplay", None))
        self.eulaBtn.setText(QCoreApplication.translate("MainWindow", u"Accept eula", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

