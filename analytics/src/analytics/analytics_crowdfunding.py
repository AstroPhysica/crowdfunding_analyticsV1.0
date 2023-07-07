import sys
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import Slot, QTranslator, QCoreApplication
from PySide6 import QtWidgets, QtCore
from analytics.user_interface import Ui_MainWindow
import pyqtgraph as pg

pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Button for selecting file
        self.ui.Selectfile.clicked.connect(self.selectfile)
        #Run analysis
        self.ui.Runanalysis.clicked.connect(self.runanalysis)

    @Slot()
    def selectfile(self):
        # Open a file dialog and get the selected file path
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName()

    @Slot()
    def runanalysis(self):
        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()