import sqlite3
from PyQt5.QtWidgets import *
import sys
from PythonProject.Qt5.Measuring_sugar_with_BD.Data import PLotUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, width=3, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.subplots()
        super(MplCanvas, self).__init__(fig)


class DlgMain1(QDialog, PLotUI.Ui_Dialog):
    def __init__(self):
        super(DlgMain1, self).__init__()
        self.setupUi(self)
        self.resize(800, 600)
        self.sugar_morning = []
        self.insulin_morning = []
        self.sugar_afternoon = []
        self.insulin_afternoon = []
        self.sugar_evening = []
        self.insulin_evening = []
        self.all_dates = []

        self.get_val_from_db(7)

        self.sc = MplCanvas(width=5, height=4, dpi=100)

        self.verticalLayout.addWidget(self.sc)

        self.btnOKMyPlots.clicked.connect(self.evt_btn_ok_clicked)
        self.btn7days.clicked.connect(self.evt_btn_7days_clicked)
        self.btn7days_2.clicked.connect(self.evt_btn_30days_clicked)

        self.evt_btn_7days_clicked()

    def evt_btn_ok_clicked(self):
        DlgMain1.close(self)

    def evt_btn_7days_clicked(self):
        self.clear_values()
        self.sc.axes.clear()
        self.resize(900, 599)
        self.get_val_from_db(7)
        width = 0.33
        len_dates = np.arange(len(self.all_dates))

        x1 = np.arange(len(self.all_dates))
        x2 = np.arange(len(self.all_dates))
        x3 = np.arange(len(self.all_dates))
        self.sc.axes.bar(x1 - width / 2, self.sugar_morning, width=width, color="royalblue",
                         label="Sugar Morning")
        self.sc.axes.bar(x2 + width / 2, self.sugar_afternoon, width=width, color="gold",
                         label="Sugar Afternoon")
        self.sc.axes.bar(x3, self.sugar_evening, width=0.2, color="violet",
                         label="Sugar Evening")
        self.sc.axes.plot(x1, self.insulin_morning, label="Insulin Morning", marker='o', ms=10, color='white',
                          mfc='royalblue')
        self.sc.axes.plot(x2, self.insulin_afternoon, label="Insulin Afternoon", marker='o', ms=10, color='white',
                          mfc='gold')
        self.sc.axes.plot(x3, self.insulin_evening, label="Insulin Evening", marker='o', ms=10, color='white', mfc='violet')
        self.sc.axes.set_xticks(len_dates, self.all_dates)

        self.sc.axes.axes.set_ylim(3)
        self.sc.axes.set_ylabel("Value sugar                Insulin Value")
        self.sc.axes.set_xlabel("Date")
        self.sc.axes.legend()

    def evt_btn_30days_clicked(self):
        self.sc.axes.clear()
        self.resize(900, 598)
        self.clear_values()
        self.get_val_from_db(30)

        width = 0.33

        x1 = np.arange(len(self.all_dates))
        x2 = np.arange(len(self.all_dates))
        x3 = np.arange(len(self.all_dates))
        self.sc.axes.bar(x1 - width / 2, self.sugar_morning, width=width, color="royalblue",
                         label="Sugar Morning")
        self.sc.axes.bar(x2 + width / 2, self.sugar_afternoon, width=width, color="gold",
                         label="Sugar Afternoon")
        self.sc.axes.bar(x3, self.sugar_evening, width=0.2, color="violet",
                         label="Sugar Evening")
        self.sc.axes.plot(x1, self.insulin_morning, label="Insulin Morning", marker='o',
                          ms=10, color='white', mfc='royalblue')
        self.sc.axes.plot(x2, self.insulin_afternoon, marker='o', ms=10, color='white',
                          mfc='gold', label="Insulin Afternoon")
        self.sc.axes.plot(x3, self.insulin_evening, marker='o', ms=10, color='white',
                          mfc='violet', label="Insulin Evening")
        self.sc.axes.set_xticks([], [])

        self.sc.axes.axes.set_ylim(3)
        self.sc.axes.set_ylabel("Value sugar                Insulin Value")
        self.sc.axes.set_xlabel("Date")
        self.sc.axes.legend()

    def clear_values(self):
        self.sugar_morning.clear()
        self.insulin_morning.clear()
        self.sugar_afternoon.clear()
        self.insulin_afternoon.clear()
        self.sugar_evening.clear()
        self.insulin_evening.clear()
        self.all_dates.clear()

    def get_val_from_db(self, limit):
        with sqlite3.connect('Data/Sugar_DB.db') as db:
            cur = db.cursor()
            query = f'''SELECT * 
                FROM sugar_mesuaring
                ORDER BY musuaring_id ASC 
                LIMIT {limit} '''
            cur.execute(query)
            db_val = cur.fetchall()
            db.commit()
            for val in db_val:
                self.all_dates.append(val[1])
                self.sugar_morning.append(val[2])
                self.insulin_morning.append(val[3])
                self.sugar_afternoon.append(val[4])
                self.insulin_afternoon.append(val[5])
                self.sugar_evening.append(val[6])
                self.insulin_evening.append(val[7])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain1()
    dlg_main.show()
    sys.exit(app.exec_())
