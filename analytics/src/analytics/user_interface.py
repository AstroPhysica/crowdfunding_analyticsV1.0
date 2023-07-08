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
    QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 842)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 10, 1111, 791))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(120, 340, 191, 163))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Gemiddelde = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde.setObjectName(u"label_Gemiddelde")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Gemiddelde)

        self.label_Gemiddelde_Leen = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde_Leen.setObjectName(u"label_Gemiddelde_Leen")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Gemiddelde_Leen)

        self.Gemiddelde_Leen_value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Leen_value.setObjectName(u"Gemiddelde_Leen_value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Gemiddelde_Leen_value)

        self.label_Gemiddelde_Donatie = QLabel(self.formLayoutWidget)
        self.label_Gemiddelde_Donatie.setObjectName(u"label_Gemiddelde_Donatie")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Gemiddelde_Donatie)

        self.Gemiddelde_Donatie_Value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Donatie_Value.setObjectName(u"Gemiddelde_Donatie_Value")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Gemiddelde_Donatie_Value)

        self.label_Totaal = QLabel(self.formLayoutWidget)
        self.label_Totaal.setObjectName(u"label_Totaal")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_Totaal)

        self.Totaal_Value = QLineEdit(self.formLayoutWidget)
        self.Totaal_Value.setObjectName(u"Totaal_Value")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Totaal_Value)

        self.label_Verwachting = QLabel(self.formLayoutWidget)
        self.label_Verwachting.setObjectName(u"label_Verwachting")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_Verwachting)

        self.Verwachting_Value = QLineEdit(self.formLayoutWidget)
        self.Verwachting_Value.setObjectName(u"Verwachting_Value")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Verwachting_Value)

        self.Gemiddelde_Value = QLineEdit(self.formLayoutWidget)
        self.Gemiddelde_Value.setObjectName(u"Gemiddelde_Value")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Gemiddelde_Value)

        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 20, 311, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.Alles = QCheckBox(self.verticalLayoutWidget)
        self.Alles.setObjectName(u"Alles")

        self.verticalLayout.addWidget(self.Alles)

        self.Gemiddelde = QCheckBox(self.verticalLayoutWidget)
        self.Gemiddelde.setObjectName(u"Gemiddelde")

        self.verticalLayout.addWidget(self.Gemiddelde)

        self.GemiddeldeLeen = QCheckBox(self.verticalLayoutWidget)
        self.GemiddeldeLeen.setObjectName(u"GemiddeldeLeen")

        self.verticalLayout.addWidget(self.GemiddeldeLeen)

        self.GemiddeldeDonatie = QCheckBox(self.verticalLayoutWidget)
        self.GemiddeldeDonatie.setObjectName(u"GemiddeldeDonatie")

        self.verticalLayout.addWidget(self.GemiddeldeDonatie)

        self.Total = QCheckBox(self.verticalLayoutWidget)
        self.Total.setObjectName(u"Total")

        self.verticalLayout.addWidget(self.Total)

        self.Verwachtingsdatum = QCheckBox(self.verticalLayoutWidget)
        self.Verwachtingsdatum.setObjectName(u"Verwachtingsdatum")

        self.verticalLayout.addWidget(self.Verwachtingsdatum)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Leen = QCheckBox(self.verticalLayoutWidget)
        self.Leen.setObjectName(u"Leen")

        self.verticalLayout_2.addWidget(self.Leen)

        self.Donatie = QCheckBox(self.verticalLayoutWidget)
        self.Donatie.setObjectName(u"Donatie")

        self.verticalLayout_2.addWidget(self.Donatie)

        self.Verwachting_Grafiek = QCheckBox(self.verticalLayoutWidget)
        self.Verwachting_Grafiek.setObjectName(u"Verwachting_Grafiek")

        self.verticalLayout_2.addWidget(self.Verwachting_Grafiek)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.label_Doel = QLabel(self.verticalLayoutWidget)
        self.label_Doel.setObjectName(u"label_Doel")

        self.horizontalLayout.addWidget(self.label_Doel)

        self.Doel = QSpinBox(self.verticalLayoutWidget)
        self.Doel.setObjectName(u"Doel")

        self.horizontalLayout.addWidget(self.Doel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Selectfile = QPushButton(self.tab)
        self.Selectfile.setObjectName(u"Selectfile")
        self.Selectfile.setGeometry(QRect(10, 20, 93, 28))
        self.Runanalysis = QPushButton(self.tab)
        self.Runanalysis.setObjectName(u"Runanalysis")
        self.Runanalysis.setGeometry(QRect(10, 70, 93, 28))
        self.Clear_button = QPushButton(self.tab)
        self.Clear_button.setObjectName(u"Clear_button")
        self.Clear_button.setGeometry(QRect(10, 120, 93, 28))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graphicsView = PlotWidget(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 10, 551, 521))
        self.graphicsView_2 = PlotWidget(self.tab_2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(560, 10, 541, 521))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Gemiddelde.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde:", None))
        self.label_Gemiddelde_Leen.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: Leen", None))
        self.label_Gemiddelde_Donatie.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: Donatie", None))
        self.label_Totaal.setText(QCoreApplication.translate("MainWindow", u"Totaal:", None))
        self.label_Verwachting.setText(QCoreApplication.translate("MainWindow", u"Verwachting:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Geef de waarden op die berekent moeten worden", None))
        self.Alles.setText(QCoreApplication.translate("MainWindow", u"Alles", None))
        self.Gemiddelde.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde", None))
        self.GemiddeldeLeen.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: leen", None))
        self.GemiddeldeDonatie.setText(QCoreApplication.translate("MainWindow", u"Gemiddelde: donatie", None))
        self.Total.setText(QCoreApplication.translate("MainWindow", u"Totaal", None))
        self.Verwachtingsdatum.setText(QCoreApplication.translate("MainWindow", u"Verwachtingsdatum bereiken doel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Staafdiagram", None))
        self.Leen.setText(QCoreApplication.translate("MainWindow", u"Leen", None))
        self.Donatie.setText(QCoreApplication.translate("MainWindow", u"Donatie", None))
        self.Verwachting_Grafiek.setText(QCoreApplication.translate("MainWindow", u"Verwachting", None))
        self.label_Doel.setText(QCoreApplication.translate("MainWindow", u"Doel:", None))
        self.Selectfile.setText(QCoreApplication.translate("MainWindow", u"Kies Bestand", None))
        self.Runanalysis.setText(QCoreApplication.translate("MainWindow", u"Run Analyse", None))
        self.Clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Diagram", None))
    # retranslateUi

