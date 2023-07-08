# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 842)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Selectfile = QPushButton(self.centralwidget)
        self.Selectfile.setObjectName(u"Selectfile")
        self.Selectfile.setGeometry(QRect(820, 30, 93, 28))
        self.Runanalysis = QPushButton(self.centralwidget)
        self.Runanalysis.setObjectName(u"Runanalysis")
        self.Runanalysis.setGeometry(QRect(820, 70, 93, 28))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(30, 30, 771, 601))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(810, 110, 291, 184))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.Gemiddelde = QCheckBox(self.verticalLayoutWidget)
        self.Gemiddelde.setObjectName(u"Gemiddelde")

        self.verticalLayout.addWidget(self.Gemiddelde)

        self.GemiddeldeLeen = QCheckBox(self.verticalLayoutWidget)
        self.GemiddeldeLeen.setObjectName(u"GemiddeldeLeen")

        self.verticalLayout.addWidget(self.GemiddeldeLeen)

        self.GemiddeldeDonatie = QCheckBox(self.verticalLayoutWidget)
        self.GemiddeldeDonatie.setObjectName(u"GemiddeldeDonatie")

        self.verticalLayout.addWidget(self.GemiddeldeDonatie)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.Verwachtingsdatum = QCheckBox(self.verticalLayoutWidget)
        self.Verwachtingsdatum.setObjectName(u"Verwachtingsdatum")

        self.verticalLayout.addWidget(self.Verwachtingsdatum)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_Doel = QLabel(self.verticalLayoutWidget)
        self.label_Doel.setObjectName(u"label_Doel")

        self.horizontalLayout.addWidget(self.label_Doel)

        self.Doel = QSpinBox(self.verticalLayoutWidget)
        self.Doel.setObjectName(u"Doel")

        self.horizontalLayout.addWidget(self.Doel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 640, 191, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Gemiddelde_Donatie = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde_Donatie.setObjectName(u"label_Gemiddelde_Donatie")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Gemiddelde_Donatie)

        self.Gemiddelde_Donatie_Value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Donatie_Value.setObjectName(u"Gemiddelde_Donatie_Value")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Gemiddelde_Donatie_Value)

        self.Gemiddelde_Value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Value.setObjectName(u"Gemiddelde_Value")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Gemiddelde_Value)

        self.Gemiddelde_Leen_value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Leen_value.setObjectName(u"Gemiddelde_Leen_value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Gemiddelde_Leen_value)

        self.Totaal_Value = QLineEdit(self.formLayoutWidget)
        self.Totaal_Value.setObjectName(u"Totaal_Value")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Totaal_Value)

        self.Verwachting_Value = QLineEdit(self.formLayoutWidget)
        self.Verwachting_Value.setObjectName(u"Verwachting_Value")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Verwachting_Value)

        self.label_Gemiddelde = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde.setObjectName(u"label_Gemiddelde")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Gemiddelde)

        self.label_Gemiddelde_Leen = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde_Leen.setObjectName(u"label_Gemiddelde_Leen")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Gemiddelde_Leen)

        self.label_Totaal = QLabel(self.formLayoutWidget)
        self.label_Totaal.setObjectName(u"label_Totaal")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_Totaal)

        self.label_Verwachting = QLabel(self.formLayoutWidget)
        self.label_Verwachting.setObjectName(u"label_Verwachting")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_Verwachting)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(810, 290, 291, 141))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Alles = QCheckBox(self.verticalLayoutWidget_2)
        self.Alles.setObjectName(u"Alles")

        self.verticalLayout_2.addWidget(self.Alles)

        self.Leen = QCheckBox(self.verticalLayoutWidget_2)
        self.Leen.setObjectName(u"Leen")

        self.verticalLayout_2.addWidget(self.Leen)

        self.Donatie = QCheckBox(self.verticalLayoutWidget_2)
        self.Donatie.setObjectName(u"Donatie")

        self.verticalLayout_2.addWidget(self.Donatie)

        self.Verwachting_Grafiek = QCheckBox(self.verticalLayoutWidget_2)
        self.Verwachting_Grafiek.setObjectName(u"Verwachting_Grafiek")

        self.verticalLayout_2.addWidget(self.Verwachting_Grafiek)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Selectfile.setText(QCoreApplication.translate("MainWindow", u"Kies Bestand", None))
        self.Runanalysis.setText(QCoreApplication.translate("MainWindow", u"Run Analyse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Geef de waarden op die berekent moeten worden", None))
        self.Gemiddelde.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde", None))
        self.GemiddeldeLeen.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: leen", None))
        self.GemiddeldeDonatie.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: donatie", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Totaal", None))
        self.Verwachtingsdatum.setText(QCoreApplication.translate("MainWindow", u"Verwachtingsdatum bereiken doel", None))
        self.label_Doel.setText(QCoreApplication.translate("MainWindow", u"Doel:", None))
        self.label_Gemiddelde_Donatie.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: Donatie", None))
        self.label_Gemiddelde.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde:", None))
        self.label_Gemiddelde_Leen.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: Leen", None))
        self.label_Totaal.setText(QCoreApplication.translate("MainWindow", u"Totaal:", None))
        self.label_Verwachting.setText(QCoreApplication.translate("MainWindow", u"Verwachting:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Staafdiagram", None))
        self.Alles.setText(QCoreApplication.translate("MainWindow", u"Alles", None))
        self.Leen.setText(QCoreApplication.translate("MainWindow", u"Leen", None))
        self.Donatie.setText(QCoreApplication.translate("MainWindow", u"Donatie", None))
        self.Verwachting_Grafiek.setText(QCoreApplication.translate("MainWindow", u"Verwachting", None))
    # retranslateUi

