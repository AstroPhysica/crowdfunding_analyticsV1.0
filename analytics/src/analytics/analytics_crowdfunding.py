import sys
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import Slot, QTranslator, QCoreApplication, QDate, Qt
from PySide6 import QtWidgets, QtCore
from analytics.user_interface import Ui_MainWindow
import pyqtgraph as pg
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #starting values
        self.check = 0

        #Button for selecting file
        self.ui.Selectfile.clicked.connect(self.selectfile)

        #Run analysis
        self.ui.Runanalysis.clicked.connect(self.runanalysis)

        #Clear checkboxes and line edits
        self.ui.Clear_button.clicked.connect(self.clear)

        #set range for spinboxes
        self.ui.Doel.setMinimum(0)
        self.ui.Doel.setMaximum(10000000)
        self.ui.Doel.setSingleStep(10000)

        #Disable text editting
        self.ui.Gemiddelde_Value.setReadOnly(True)
        self.ui.Gemiddelde_Donatie_Value.setReadOnly(True)
        self.ui.Gemiddelde_Leen_value.setReadOnly(True)
        self.ui.Totaal_Value.setReadOnly(True)
        self.ui.Verwachting_Value.setReadOnly(True)
        #Set initial text
        self.ui.Gemiddelde_Value.setText('\u20ac')
        self.ui.Gemiddelde_Leen_value.setText('\u20ac')
        self.ui.Gemiddelde_Donatie_Value.setText('\u20ac')
        self.ui.Totaal_Value.setText('\u20ac')
        self.ui.Verwachting_Value.setText('dd-mm-yyyy')

    @Slot()
    def clear(self):
        #clear values
        self.ui.Gemiddelde_Value.clear()
        self.ui.Gemiddelde_Leen_value.clear()
        self.ui.Gemiddelde_Donatie_Value.clear()
        self.ui.Totaal_Value.clear()
        self.ui.Verwachting_Value.clear()
        #clear checkboxes
        self.ui.Gemiddelde.setChecked(False)
        self.ui.GemiddeldeDonatie.setChecked(False)
        self.ui.GemiddeldeLeen.setChecked(False)
        self.ui.Total.setChecked(False)
        self.ui.Verwachtingsdatum.setChecked(False)
        self.ui.Alles.setChecked(False)

    @Slot()
    def selectfile(self):
        # Open a file dialog and get the selected file path
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName()
        if self.file_path is None:
            self.check = 0
        else:
            self.check = 1

    @Slot()
    def runanalysis(self):
        #load csv file to dataframe
        df = pd.read_csv(self.file_path)
        #Arange the dataframe in chronological order
        df['Datum'] = pd.to_datetime(df['Datum'])
        df = df.sort_values('Datum')
        if self.check == 0:
            print("WAARSCHUWING: Geen bestand gekozen")
        else:
            if self.ui.Alles.isChecked():
                print('Bestand word verwerkt......')

                #Compute all mean values
                leen = []
                donatie = []
                for i in range(len(df.iloc[:, 1])):
                    if df['Leen_Donatie'].iloc[i] == "leen":
                        leen.append(df['Bedrag'].iloc[i])
                    if df['Leen_Donatie'].iloc[i] == "donatie":
                        donatie.append(df['Bedrag'].iloc[i])
                gemiddelde = round(np.mean(df['Bedrag']), 2)
                leen = np.array(leen)
                gemiddelde_leen = round(np.mean(leen), 2)
                donatie = np.array(donatie)
                gemiddelde_donatie = round(np.mean(donatie), 2)

                #compute total value
                totaal = np.sum(df['Bedrag'])

                #Predict reaching set target
                time_delta = df['Datum'].iloc[-1] - df['Datum'].iloc[0]
                time_delta = time_delta.days
                totaal = np.sum(df['Bedrag'])
                voordering = totaal/time_delta
                doel = self.ui.Doel.value()
                dagen = (doel - totaal)/voordering
                bereik_doel = df['Datum'].iloc[-1] + timedelta(days=dagen)

                #setting computed values
                self.ui.Gemiddelde_Value.setText(f'\u20ac {gemiddelde}')
                self.ui.Gemiddelde_Donatie_Value.setText(f'\u20ac {gemiddelde_donatie}')
                self.ui.Gemiddelde_Leen_value.setText(f'\u20ac {gemiddelde_leen}')
                self.ui.Totaal_Value.setText(f'\u20ac {totaal}')
                self.ui.Verwachting_Value.setText(f'\u20ac {bereik_doel.day}-{bereik_doel.month}-{bereik_doel.year}')
            else:
                if self.ui.Gemiddelde.isChecked():
                    gemiddelde = round(np.mean(df['Bedrag']), 2)
                    self.ui.Gemiddelde_Value.setText(f'\u20ac {gemiddelde}')
                if self.ui.GemiddeldeDonatie.isChecked():
                    donatie = []
                    for i in range(len(df.iloc[:, 1])):    
                        if df['Leen_Donatie'].iloc[i] == "donatie":
                            donatie.append(df['Bedrag'].iloc[i])
                    donatie = np.array(donatie)
                    gemiddelde_leen = round(np.mean(donatie), 2)
                    self.ui.Gemiddelde_Donatie_Value.setText(f'\u20ac {gemiddelde_donatie}')
                if self.ui.GemiddeldeLeen.isChecked():
                    leen = []
                    for i in range(len(df.iloc[:, 1])):
                        if df['Leen_Donatie'].iloc[i] == "leen":
                            leen.append(df['Bedrag'].iloc[i])
                    leen = np.array(leen)
                    gemiddelde_leen = round(np.mean(leen), 2)
                    self.ui.Gemiddelde_Leen_value.setText(f'\u20ac {gemiddelde_leen}')
                if self.ui.Total.isChecked():
                    totaal = np.sum(df['Bedrag'])
                    self.ui.Totaal_Value.setText(f'\u20ac {totaal}')
                if self.ui.Verwachtingsdatum.isChecked():
                    time_delta = df['Datum'].iloc[-1] - df['Datum'].iloc[0]
                    time_delta = time_delta.days
                    totaal = np.sum(df['Bedrag'])
                    voordering = totaal/time_delta
                    doel = self.ui.Doel.value()
                    dagen = (doel - totaal)/voordering
                    bereik_doel = df['Datum'].iloc[-1] + timedelta(days=dagen)
                    self.ui.Verwachting_Value.setText(f'\u20ac {bereik_doel.day}-{bereik_doel.month}-{bereik_doel.year}')
        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()