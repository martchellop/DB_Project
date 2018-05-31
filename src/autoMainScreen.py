# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lauging-gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(400, 20, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 oblique 20pt \"Cantarell\";\n"
"color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 401, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.combo_box_choose_event_type = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_box_choose_event_type.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.combo_box_choose_event_type.setObjectName("combo_box_choose_event_type")
        self.combo_box_choose_event_type.addItem("")
        self.combo_box_choose_event_type.addItem("")
        self.combo_box_choose_event_type.addItem("")
        self.horizontalLayout.addWidget(self.combo_box_choose_event_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.date_edit_start = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date_edit_start.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.date_edit_start.setCalendarPopup(False)
        self.date_edit_start.setObjectName("date_edit_start")
        self.horizontalLayout_2.addWidget(self.date_edit_start)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.date_edit_end = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date_edit_end.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.date_edit_end.setObjectName("date_edit_end")
        self.horizontalLayout_2.addWidget(self.date_edit_end)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(200, 20))
        self.label_8.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.line_edit_cpf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_edit_cpf.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.line_edit_cpf.setClearButtonEnabled(False)
        self.line_edit_cpf.setObjectName("line_edit_cpf")
        self.horizontalLayout_3.addWidget(self.line_edit_cpf)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        self.label_9.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.line_edit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_edit_name.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.line_edit_name.setInputMask("")
        self.line_edit_name.setText("")
        self.line_edit_name.setMaxLength(32767)
        self.line_edit_name.setObjectName("line_edit_name")
        self.horizontalLayout_4.addWidget(self.line_edit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.button_search_events = QtWidgets.QPushButton(self.centralWidget)
        self.button_search_events.setGeometry(QtCore.QRect(160, 590, 131, 51))
        self.button_search_events.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_search_events.setObjectName("button_search_events")
        self.table_search_results = QtWidgets.QTableView(self.centralWidget)
        self.table_search_results.setGeometry(QtCore.QRect(500, 100, 551, 631))
        self.table_search_results.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.table_search_results.setObjectName("table_search_results")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Pesquisar Eventos</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Tipo</p></body></html>"))
        self.combo_box_choose_event_type.setItemText(0, _translate("MainWindow", "Ambos"))
        self.combo_box_choose_event_type.setItemText(1, _translate("MainWindow", "Casamento"))
        self.combo_box_choose_event_type.setItemText(2, _translate("MainWindow", "Festa"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Entre</p></body></html>"))
        self.date_edit_start.setDisplayFormat(_translate("MainWindow", "dd/mm/yyyy"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>e</p></body></html>"))
        self.date_edit_end.setDisplayFormat(_translate("MainWindow", "dd/mm/yyyy"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Organizador-CPF</p></body></html>"))
        self.line_edit_cpf.setInputMask(_translate("MainWindow", "999.999.999.99"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Organizador-Nome</p></body></html>"))
        self.button_search_events.setText(_translate("MainWindow", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

