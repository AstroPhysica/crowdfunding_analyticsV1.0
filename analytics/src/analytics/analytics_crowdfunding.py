import sys
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import Slot, QTranslator, QCoreApplication
from PySide6 import QtWidgets, QtCore
from analytics.user_interface import Ui_MainWindow
import pyqtgraph as pg
import pandas as pd
import numpy as np

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
        df = pd.read_csv(self.file_path)
        if self.check == 0:
            print("WAARSCHUWING: Geen bestand gekozen")
        else:
            #Alles is checked
            if self.ui.Alles.isChecked:
                print('Bestand word verwerkt......')

                #Compute all mean values
                leen = []
                donatie = []
                for i in range(len(df.iloc[:, 1])):
                    if df.iloc[:, 1][i] == "leen":
                        leen.append(df.iloc[:, 0][i])
                    if df.iloc[:, 1][i] == "donatie":
                        donatie.append(df.iloc[:, 0][i])
                gemiddelde = np.mean(df.iloc[:,0])
                leen = np.array(leen)
                gemiddelde_leen = np.mean(leen)
                donatie = np.array(donatie)
                gemiddelde_donatie = np.mean(donatie)
                
        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()