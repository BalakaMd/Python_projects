# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgMain(object):
    def setupUi(self, dlgMain):
        dlgMain.setObjectName("dlgMain")
        dlgMain.resize(605, 438)
        dlgMain.setWindowTitle("Measuring Sugar")
        self.centralwidget = QtWidgets.QWidget(dlgMain)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblGreeding = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.lblGreeding.setFont(font)
        self.lblGreeding.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGreeding.setObjectName("lblGreeding")
        self.verticalLayout_4.addWidget(self.lblGreeding)
        self.btnAddNewSugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddNewSugar.setDefault(True)
        self.btnAddNewSugar.setObjectName("btnAddNewSugar")
        self.verticalLayout_4.addWidget(self.btnAddNewSugar)
        self.layForm = QtWidgets.QFormLayout()
        self.layForm.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layForm.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.layForm.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.layForm.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layForm.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layForm.setObjectName("layForm")
        self.lblEnterSugar = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterSugar.setObjectName("lblEnterSugar")
        self.layForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblEnterSugar)
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setObjectName("dateLabel")
        self.layForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dteDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dteDateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dteDateEdit.setCalendarPopup(True)
        self.dteDateEdit.setCurrentSectionIndex(0)
        self.dteDateEdit.setObjectName("dteDateEdit")
        self.layForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dteDateEdit)
        self.lblPartOfDay = QtWidgets.QLabel(self.centralwidget)
        self.lblPartOfDay.setObjectName("lblPartOfDay")
        self.layForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblPartOfDay)
        self.cmbPartOfDay = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPartOfDay.setObjectName("cmbPartOfDay")
        self.cmbPartOfDay.addItem("")
        self.cmbPartOfDay.addItem("")
        self.cmbPartOfDay.addItem("")
        self.layForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbPartOfDay)
        self.lblComments = QtWidgets.QLabel(self.centralwidget)
        self.lblComments.setObjectName("lblComments")
        self.layForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblComments)
        self.commentsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.commentsLineEdit.setObjectName("commentsLineEdit")
        self.layForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commentsLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.horizontalLayout.addWidget(self.btnBox)
        self.layForm.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.dsbEnterSugar = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dsbEnterSugar.setEnabled(True)
        self.dsbEnterSugar.setWrapping(False)
        self.dsbEnterSugar.setDecimals(1)
        self.dsbEnterSugar.setMaximum(40.0)
        self.dsbEnterSugar.setSingleStep(0.10)
        self.dsbEnterSugar.setProperty("value", 6.5)
        self.dsbEnterSugar.setObjectName("dsbEnterSugar")
        self.layForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dsbEnterSugar)
        self.verticalLayout_4.addLayout(self.layForm)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2, 1)
        dlgMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dlgMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 24))
        self.menubar.setObjectName("menubar")
        dlgMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dlgMain)
        self.statusbar.setObjectName("statusbar")
        dlgMain.setStatusBar(self.statusbar)

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)

    def retranslateUi(self, dlgMain):
        _translate = QtCore.QCoreApplication.translate
        dlgMain.setWindowTitle(_translate("dlgMain", "MainWindow"))
        self.lblGreeding.setText(_translate("dlgMain", "TextLabel"))
        self.btnAddNewSugar.setText(_translate("dlgMain", "Add new sugar"))
        self.lblEnterSugar.setText(_translate("dlgMain", "Enter sugar"))
        self.dateLabel.setText(_translate("dlgMain", "Date"))
        self.lblPartOfDay.setText(_translate("dlgMain", "Part of Day"))
        self.cmbPartOfDay.setItemText(0, _translate("dlgMain", "Morning"))
        self.cmbPartOfDay.setItemText(1, _translate("dlgMain", "Afternoon"))
        self.cmbPartOfDay.setItemText(2, _translate("dlgMain", "Evening"))
        self.lblComments.setText(_translate("dlgMain", "Comments"))
        self.dsbEnterSugar.setSuffix(_translate("dlgMain", " mmol/L"))
        self.pushButton.setText(_translate("dlgMain", "ShowGraf"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgMain = QtWidgets.QMainWindow()
    ui = Ui_dlgMain()
    ui.setupUi(dlgMain)
    dlgMain.show()
    sys.exit(app.exec_())
