import sys
from PySide6.QtWidgets import QApplication, QGraphicsScene, QFileDialog
from PySide6.QtCore import Slot, QTranslator, QCoreApplication, QDate, Qt
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPainter, QBrush
from analytics.user_interface import Ui_MainWindow
import pyqtgraph as pg
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.metrics import mean_squared_error

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
        self.ui.Totaal_Leen_Value.setReadOnly(True)
        self.ui.Totaal_Donatie_Value.setReadOnly(True)

        #Set initial text
        self.ui.Gemiddelde_Value.setText('\u20ac')
        self.ui.Gemiddelde_Leen_value.setText('\u20ac')
        self.ui.Gemiddelde_Donatie_Value.setText('\u20ac')
        self.ui.Totaal_Value.setText('\u20ac')
        self.ui.Totaal_Leen_Value.setText('\u20ac')
        self.ui.Totaal_Donatie_Value.setText('\u20ac')
        self.ui.Verwachting_Value.setText('dd-mm-yyyy')

        #graphics
        Totals_plot = self.ui.Totals
        age_groups_plot = self.ui.age_groups
    
    @Slot()
    def clear(self):
        #clear values
        self.ui.Gemiddelde_Value.clear()
        self.ui.Gemiddelde_Leen_value.clear()
        self.ui.Gemiddelde_Donatie_Value.clear()
        self.ui.Totaal_Value.clear()
        self.ui.Verwachting_Value.clear()
        self.ui.Totaal_Donatie_Value.clear()
        self.ui.Totaal_Leen_Value.clear()
        #clear checkboxes
        self.ui.Gemiddelde.setChecked(False)
        self.ui.GemiddeldeDonatie.setChecked(False)
        self.ui.GemiddeldeLeen.setChecked(False)
        self.ui.Total.setChecked(False)
        self.ui.Verwachtingsdatum.setChecked(False)
        self.ui.Alles.setChecked(False)
        self.ui.Total_Donatie.setChecked(False)
        self.ui.Total_Leen.setChecked(False)    
        self.ui.Totalen_Graph.setChecked(False)
        self.ui.Age_groups_Graph.setChecked(False)
        self.ui.Opslaan.setChecked(False)

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

                #Setting computed values
                self.ui.Gemiddelde_Value.setText(f'\u20ac {gemiddelde}')
                self.ui.Gemiddelde_Donatie_Value.setText(f'\u20ac {gemiddelde_donatie}')
                self.ui.Gemiddelde_Leen_value.setText(f'\u20ac {gemiddelde_leen}')
                self.ui.Totaal_Value.setText(f'\u20ac {totaal}')
                self.ui.Verwachting_Value.setText(f'\u20ac {bereik_doel.day}-{bereik_doel.month}-{bereik_doel.year}')
                self.ui.Totaal_Donatie_Value.setText(f'\u20ac {sum(donatie)}')
                self.ui.Totaal_Leen_Value.setText(f'\u20ac {sum(leen)}')

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
                    gemiddelde_donatie = round(np.mean(donatie), 2)
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
                if self.ui.Total_Donatie.isChecked():
                    donatie = []
                    for i in range(len(df.iloc[:, 1])):
                        if df['Leen_Donatie'].iloc[i] == "donatie":
                            donatie.append(df['Bedrag'].iloc[i])
                    self.ui.Totaal_Donatie_Value.setText(f'\u20ac {sum(donatie)}')
                if self.ui.Total_Leen.isChecked():
                    leen = []
                    for i in range(len(df.iloc[:, 1])):
                        if df['Leen_Donatie'].iloc[i] == "leen":
                            leen.append(df['Bedrag'].iloc[i])
                    self.ui.Totaal_Leen_Value.setText(f'\u20ac {sum(leen)}')
            # Creates all the graphics        
            if self.ui.Totalen_Graph.isChecked():
                dates = df['Datum'].iloc
                dates_no_duplicate = set(date.date() for date in dates)
                dates_array = sorted(list(dates_no_duplicate))
                totals = np.zeros(len(dates_array))

                #create data for each bar in barchart
                for i in range(0, len(dates_array)):
                    dates_list = []
                    for j in range(0, df.shape[0]):
                        if dates_array[i] == datetime.date(df['Datum'].iloc[j]):
                             dates_list.append(df['Bedrag'].iloc[j])
                    Sum = sum(dates_list)
                    if i == 0:
                        totals[i] = Sum
                    else:
                        totals[i] = Sum + totals[i-1]
                #changing totals from array to list
                totals_list = totals.tolist()

                #create figure
                target_line = []
                fig = Figure(figsize=(17, 8), dpi=100)
                ax = fig.add_subplot(111)
                #create predictions

                #first prediction: Linear prediction
                # Calculate time delta and total amount
                time_delta = (df['Datum'].iloc[-1] - df['Datum'].iloc[0]).days
                totaal = np.sum(df['Bedrag'])

                # Calculate average rate of increase
                voordering = totaal / time_delta

                # Retrieve goal and calculate remaining days
                doel = self.ui.Doel.value()
                dagen = (doel - totaal) / voordering

                # Calculate target date
                bereik_doel = df['Datum'].iloc[-1].to_pydatetime() + timedelta(days=dagen)
                # Generate date range and corresponding raised amounts
                datums = pd.date_range(start=df['Datum'].iloc[0], end=bereik_doel)
                start_date = df['Datum'].iloc[0]
                start_date = start_date.to_pydatetime()
                raised = [voordering * (d - start_date).days for d in datums]
                
                #create target line
                for i in range(len(datums)):
                    target_line.append(self.ui.Doel.value())

                # Calculate the difference between consecutive dates
                date_diff = np.diff(dates_array)

                # Fill missing values with previous value
                filled_dates = []
                filled_values = []
                for i in range(len(dates_array)):
                    filled_dates.append(dates_array[i])
                    filled_values.append(totals[i])
                    
                    if i < len(date_diff):
                        num_missing_dates = (date_diff[i].days - 1)
                        for j in range(num_missing_dates):
                            filled_dates.append(dates_array[i] + timedelta(days=j+1))
                            filled_values.append(totals[i])

                #create array of dates and values that contain the previous dates and values of totals and dates_array
                previous_values = []
                for i in range(1, len(filled_dates)):
                    previous_values.append(filled_values[i-1])
                previous_dates = filled_dates.copy()
                previous_dates.pop(0)
                #create and plot the bar chart
                x = dates_array
                heights = [value for value in totals]
                ax.bar(filled_dates, filled_values, color='r', align='center', label='Newly raised')
                ax.bar(previous_dates, previous_values, color='b', align='center', label='Raised')
                ax.set_xticks(datums)
                ax.set_xticklabels(datums)
                ax.tick_params(axis='x', labelsize=6)
                date_format = mdates.DateFormatter("%d-%m")
                ax.xaxis.set_major_formatter(date_format)
                fig.autofmt_xdate()

                #plot the line plots
                ax.plot(datums, target_line, 'r--', label=f'Target: {self.ui.Doel.value()}')
                ax.plot(datums, raised, 'orange', label='linear prediction')

                #legend
                ax.legend()
                # Create the canvas for the chart
                canvas_totals = FigureCanvas(fig)
                # Get the existing QGraphicsView from the UI
                graphics_view = self.ui.Totals
                scene = QGraphicsScene()
                scene.addWidget(canvas_totals)

                # Set the QGraphicsScene on the QGraphicsView
                graphics_view.setScene(scene)
            #create age groups diagram
            if self.ui.Age_groups_Graph.isChecked():
                #make age groupse
                young = [] #18-25
                young_raised = []
                young_adults = [] #25-35
                young_adults_raised = []
                midlife_adults = [] #35-45
                midlife_adults_raised = []
                older_adults = [] #45-55
                older_adults_raised = []
                old_but_not_yet_old_adults = [] #55-65
                old_but_not_yet_old_adults_raised = []
                old_adults = [] #65+
                old_adults_raised = []
                age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64','65+']
                for i in range(len(df['Leeftijd'])):
                    if df['Leeftijd'][i] < 25:
                        young.append(df['Leeftijd'][i])
                        young_raised.append(df['Bedrag'][i])
                    if df['Leeftijd'][i] >= 25 and df['Leeftijd'][i] < 35:
                        young_adults.append(df['Leeftijd'][i])
                        young_adults_raised.append(df['Bedrag'][i])
                    if df['Leeftijd'][i] >= 35 and df['Leeftijd'][i] < 45:
                        midlife_adults.append(df['Leeftijd'][i])
                        midlife_adults_raised.append(df['Bedrag'][i])
                    if df['Leeftijd'][i] >= 45 and df['Leeftijd'][i] < 55:
                        older_adults.append(df['Leeftijd'][i])
                        older_adults_raised.append(df['Bedrag'][i])
                    if df['Leeftijd'][i] >= 55 and df['Leeftijd'][i] < 65:
                        old_but_not_yet_old_adults.append(df['Leeftijd'][i])
                        old_but_not_yet_old_adults_raised.append(df['Bedrag'][i])
                    if df['Leeftijd'][i] >= 65:
                        old_adults.append(df['Leeftijd'][i])
                        old_adults_raised.append(df['Bedrag'][i])
                    #totals raised
                    young_raised_total = sum(young_raised)
                    young_adults_raised_total = sum(young_adults_raised)
                    midlife_adults_raised_total = sum(midlife_adults_raised)
                    older_adults_raised_total = sum(older_adults_raised)
                    old_but_not_yet_old_adults_raised_total = sum(old_but_not_yet_old_adults_raised)
                    old_adults_raised_total = sum(old_adults_raised)
                    totals_raised = [young_raised_total, young_adults_raised_total, midlife_adults_raised_total, older_adults_raised_total, 
                                    old_but_not_yet_old_adults_raised_total, old_adults_raised_total]
                    #set colors for each age group
                    colors = ['blue', 'green', 'orange', 'red', 'purple', 'yellow']

                    # Set the positions of the bars on the x-axis
                    x_positions = np.arange(len(totals_raised))

                    # Create the bar chart with different colors
                    fig2 = Figure(figsize=(17, 8), dpi=100)
                    ax = fig2.add_subplot(111)
                    ax.bar(x_positions, totals_raised, color=colors)

                    # Customize the chart
                    ax.set_xlabel('Age groups')
                    ax.set_ylabel('Totals')
                    ax.set_title('Totals  by age groups')
                    ax.set_xticks(x_positions)
                    ax.set_xticklabels(age_groups)

                    # Create the canvas for the chart
                    canvas_age_groups = FigureCanvas(fig2)
                    # Get the existing QGraphicsView from the UI
                    graphics_view = self.ui.age_groups
                    scene = QGraphicsScene()
                    scene.addWidget(canvas_age_groups)

                    # Set the QGraphicsScene on the QGraphicsView
                    graphics_view.setScene(scene)

            if self.ui.Opslaan.isChecked():
                if self.ui.Totalen_Graph.isChecked():
                    fig.savefig('Totalen.png')
                if self.ui.Age_groups_Graph.isChecked():
                    fig2.savefig('age_groups.png')    
        
        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()