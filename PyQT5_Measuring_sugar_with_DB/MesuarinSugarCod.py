from PyQt5.QtCore import QDate
import sqlite3
from PyQt5.QtWidgets import *
from PythonProject.Qt5.Measuring_sugar_with_BD.Data.MeaseringSugarUI import *
from PythonProject.Qt5.Measuring_sugar_with_BD.Data import PloUICod
import sys


class DlgMain(QMainWindow, Ui_dlgMain):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)

        # General settings
        self.lblGreeding.setText("Hello Dimka")
        self.btnAddNewSugar.setDefault(True)
        self.dteDateEdit.setDate(QDate.currentDate())
        self.dsbEnterSugar.setDecimals(1)
        self.valSugar = 6.5
        self.valPartOfDay = "Morning"
        self.valComments = ""
        self.valInsulin = 10
        self.measuring_date_list = ...

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnClearTable = QPushButton("Clear Table")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.btnClearTable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.btnAddNewSugar.setDefault(True)

        self.set_all_btn_visible("F")

        # Set Table Widget
        self.tableWidget.setHorizontalHeaderLabels(["Date", "Sugar \n Morning", "Insulin \n Morning",
                                                    "Sugar \n Afternoon", "Insulin \n Afternoon",
                                                    "Sugar \n Evening", "Insulin \n Evening", "comments"])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 55)
        self.tableWidget.setColumnWidth(3, 65)
        self.tableWidget.setColumnWidth(4, 55)
        self.tableWidget.setColumnWidth(5, 60)
        self.tableWidget.setColumnWidth(6, 50)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setRowCount(0)

        # Set table value
        self.set_table_value()

        # Set event handlers
        self.btnAddNewSugar.clicked.connect(self.evt_btn_add_sugar_clicked)
        self.dsbEnterSugar.valueChanged.connect(self.evt_dsb_val_changed)
        self.cmbPartOfDay.currentIndexChanged.connect(self.evt_cmb_val_changed)
        self.btnClearTable.clicked.connect(self.evt_btn_clear_clicked)

        self.pushButton.clicked.connect(self.evt_btn_graph_clicked)
        self.btnBox.clicked.connect(self.evt_btn_box_clicked)
        self.commentsLineEdit.textChanged.connect(self.evt_led_text_changed)

        self.spbInsulin.valueChanged.connect(self.evt_cmb_insulin_val_changed)

        self.tableWidget.cellDoubleClicked.connect(self.del_tabl_item)

    def evt_btn_add_sugar_clicked(self):
        self.set_all_btn_visible('T')

    def evt_dsb_val_changed(self, val):
        self.valSugar = val

    def evt_cmb_val_changed(self, idx):
        self.valPartOfDay = self.cmbPartOfDay.itemText(idx)

    def evt_led_text_changed(self, val):
        self.valComments = val

    def evt_cmb_insulin_val_changed(self, val):
        self.valInsulin = val

    def evt_btn_box_clicked(self, val):
        if val.text() == "OK":
            self.set_all_btn_visible("T")

            self.get_measuring_date()

            self.set_val_to_db()
            self.set_table_value()
            self.set_all_btn_visible("F")
        else:
            self.set_all_btn_visible("F")

    def evt_btn_graph_clicked(self):
        dlgPlot = PloUICod.DlgMain1()
        dlgPlot.show()
        dlgPlot.exec_()

    def evt_btn_clear_clicked(self):
        res = QMessageBox.question(self, "Really?", "Do you want clear table?")
        if res == QMessageBox.Yes:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = '''DELETE from sugar_mesuaring'''
                query1 = '''DELETE from sqlite_sequence'''
                cur.execute(query)
                cur.execute(query1)
                db.commit()
        self.set_table_value()

    def set_table_value(self):
        with sqlite3.connect('Data/Sugar_DB.db') as db:
            cur = db.cursor()
            query = f'''SELECT * from sugar_mesuaring ORDER by musuaring_id DESC'''
            cur.execute(query)
            db_val = cur.fetchall()
            db.commit()
        self.tableWidget.setRowCount(len(db_val))
        count = 0
        for items in db_val:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(items[1]))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(items[2]).replace('-1.0', ' ')))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(items[3]).replace('-1', ' ')))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(items[4]).replace('-1.0', ' ')))
            self.tableWidget.setItem(count, 4, QTableWidgetItem(str(items[5]).replace('-1', ' ')))
            self.tableWidget.setItem(count, 5, QTableWidgetItem(str(items[6]).replace('-1.0', ' ')))
            self.tableWidget.setItem(count, 6, QTableWidgetItem(str(items[7]).replace('-1', ' ')))
            self.tableWidget.setItem(count, 7, QTableWidgetItem(items[8]))
            count += 1

    def get_measuring_date(self):
        with sqlite3.connect('Data/Sugar_DB.db') as db:
            cur = db.cursor()
            query = f'''SELECT mesuaring_date
                        FROM sugar_mesuaring '''
            cur.execute(query)
            val = cur.fetchall()
            db.commit()
        self.measuring_date_list = [date[0] for date in val]

    def set_val_to_db(self):
        if self.valPartOfDay == 'Morning' \
                and self.dteDateEdit.date().toString('dd MM yyyy') not in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''INSERT INTO sugar_mesuaring
                    (mesuaring_date, sugar_morning, insulin_morning, comments)
                    VALUES('{self.dteDateEdit.date().toString('dd MM yyyy')}',{float("{0:.2f}".format(self.valSugar))},
                    {float("{0:.2f}".format(self.valInsulin))}, '{self.valComments}') '''
                cur.execute(query)
                db.commit()
        elif self.valPartOfDay == 'Morning' \
                and self.dteDateEdit.date().toString('dd MM yyyy') in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''UPDATE sugar_mesuaring
                            SET sugar_morning = {float("{0:.2f}".format(self.valSugar))},
                                insulin_morning = {float("{0:.2f}".format(self.valInsulin))},
                                comments = '{self.valComments}'
                                WHERE mesuaring_date = '{self.dteDateEdit.date().toString('dd MM yyyy')}' '''
                cur.execute(query)
                db.commit()

        if self.valPartOfDay == 'Afternoon' \
                and self.dteDateEdit.date().toString('dd MM yyyy') not in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''INSERT INTO sugar_mesuaring
                    (mesuaring_date, sugar_afternoon, insulin_afternoon, comments)
                    VALUES('{self.dteDateEdit.date().toString('dd MM yyyy')}',{float("{0:.2f}".format(self.valSugar))},
                    {float("{0:.2f}".format(self.valInsulin))}, '{self.valComments}') '''
                cur.execute(query)
                db.commit()
        elif self.valPartOfDay == 'Afternoon' \
                and self.dteDateEdit.date().toString('dd MM yyyy') in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''UPDATE sugar_mesuaring
                            SET sugar_afternoon = {float("{0:.2f}".format(self.valSugar))},
                                insulin_afternoon = {float("{0:.2f}".format(self.valInsulin))},
                                comments = '{self.valComments}'
                                WHERE mesuaring_date = '{self.dteDateEdit.date().toString('dd MM yyyy')}' '''
                cur.execute(query)
                db.commit()

        if self.valPartOfDay == 'Evening' \
                and self.dteDateEdit.date().toString('dd MM yyyy') not in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''INSERT INTO sugar_mesuaring
                    (mesuaring_date, sugar_evening, insulin_evening, comments)
                    VALUES('{self.dteDateEdit.date().toString('dd MM yyyy')}',{float("{0:.2f}".format(self.valSugar))},
                    {float("{0:.2f}".format(self.valInsulin))}, '{self.valComments}') '''
                cur.execute(query)
                db.commit()
        elif self.valPartOfDay == 'Evening' \
                and self.dteDateEdit.date().toString('dd MM yyyy') in self.measuring_date_list:
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''UPDATE sugar_mesuaring
                            SET sugar_evening = {float("{0:.2f}".format(self.valSugar))},
                                insulin_evening = {float("{0:.2f}".format(self.valInsulin))},
                                comments = '{self.valComments}'
                                WHERE mesuaring_date = '{self.dteDateEdit.date().toString('dd MM yyyy')}' '''
                cur.execute(query)
                db.commit()

    def set_all_btn_visible(self, arg):
        if arg == 'T':
            self.lblEnterSugar.setVisible(True)
            self.dsbEnterSugar.setVisible(True)
            self.dateLabel.setVisible(True)
            self.dteDateEdit.setVisible(True)
            self.lblPartOfDay.setVisible(True)
            self.cmbPartOfDay.setVisible(True)
            self.lblComments.setVisible(True)
            self.commentsLineEdit.setVisible(True)
            self.btnBox.setVisible(True)
            self.lblInsulin.setVisible(True)
            self.spbInsulin.setVisible(True)
            self.btnAddNewSugar.setVisible(False)
        else:
            self.lblEnterSugar.setVisible(False)
            self.dsbEnterSugar.setVisible(False)
            self.dateLabel.setVisible(False)
            self.dteDateEdit.setVisible(False)
            self.lblPartOfDay.setVisible(False)
            self.cmbPartOfDay.setVisible(False)
            self.lblComments.setVisible(False)
            self.commentsLineEdit.setVisible(False)
            self.btnBox.setVisible(False)
            self.lblInsulin.setVisible(False)
            self.spbInsulin.setVisible(False)
            self.btnAddNewSugar.setVisible(True)

    def del_tabl_item(self, row, col):
        date = self.tableWidget.item(row, 0).text()
        col_val = ''
        if col == 0:
            res = QMessageBox.question(self, '', "Do you want to delete all data in this date ?")
            if res == QMessageBox.Yes:
                with sqlite3.connect('Data/Sugar_DB.db') as db:
                    cur = db.cursor()
                    query = f'''DELETE FROM sugar_mesuaring
                                WHERE mesuaring_date = '{date}' '''
                    cur.execute(query)
                    db.commit()
                    self.set_table_value()
                    return 1
        res = QMessageBox.question(self, '', "Do you want to delete this value?")
        if res == QMessageBox.Yes:
            print(col)
            if col == 1:
                col_val = 'sugar_morning'
            elif col == 2:
                col_val = 'insulin_morning'
            elif col == 3:
                col_val = 'sugar_afternoon'
            elif col == 4:
                col_val = 'insulin_afternoon'
            elif col == 5:
                col_val = 'sugar_evening'
            elif col == 6:
                col_val = 'insulin_evening'
            else:
                with sqlite3.connect('Data/Sugar_DB.db') as db:
                    cur = db.cursor()
                    query = f'''UPDATE sugar_mesuaring
                                SET comments = ""
                                WHERE mesuaring_date = '{date}' '''
                    cur.execute(query)
                    db.commit()
                    return 1
            with sqlite3.connect('Data/Sugar_DB.db') as db:
                cur = db.cursor()
                query = f'''UPDATE sugar_mesuaring
                            SET {col_val} = -1
                            WHERE mesuaring_date = '{date}' '''
                cur.execute(query)
                db.commit()
        self.set_table_value()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())
