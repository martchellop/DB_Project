# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateTickets.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 823)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 411, 41))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 170, 536, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_cpf = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cpf.setMinimumSize(QtCore.QSize(200, 20))
        self.label_cpf.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_cpf.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpf.setObjectName("label_cpf")
        self.horizontalLayout_3.addWidget(self.label_cpf)
        self.line_edit_cpf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_edit_cpf.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.line_edit_cpf.setClearButtonEnabled(False)
        self.line_edit_cpf.setObjectName("line_edit_cpf")
        self.horizontalLayout_3.addWidget(self.line_edit_cpf)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_data = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_data.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.setObjectName("label_data")
        self.horizontalLayout_2.addWidget(self.label_data)
        self.date_edit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date_edit.setAutoFillBackground(False)
        self.date_edit.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.date_edit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 11), QtCore.QTime(0, 0, 0)))
        self.date_edit.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.date_edit.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setCurrentSectionIndex(0)
        self.date_edit.setDate(QtCore.QDate(2018, 1, 11))
        self.date_edit.setObjectName("date_edit")
        self.horizontalLayout_2.addWidget(self.date_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ticket_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ticket_number.sizePolicy().hasHeightForWidth())
        self.label_ticket_number.setSizePolicy(sizePolicy)
        self.label_ticket_number.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_ticket_number.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_ticket_number.setObjectName("label_ticket_number")
        self.horizontalLayout.addWidget(self.label_ticket_number)
        self.line_edit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_id.sizePolicy().hasHeightForWidth())
        self.line_edit_id.setSizePolicy(sizePolicy)
        self.line_edit_id.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.line_edit_id.setClearButtonEnabled(False)
        self.line_edit_id.setObjectName("line_edit_id")
        self.horizontalLayout.addWidget(self.line_edit_id)
        self.choose_type = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_type.sizePolicy().hasHeightForWidth())
        self.choose_type.setSizePolicy(sizePolicy)
        self.choose_type.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.choose_type.setObjectName("choose_type")
        self.choose_type.addItem("")
        self.choose_type.addItem("")
        self.horizontalLayout.addWidget(self.choose_type)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.button_update_event = QtWidgets.QPushButton(self.centralWidget)
        self.button_update_event.setGeometry(QtCore.QRect(390, 420, 131, 51))
        self.button_update_event.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_update_event.setObjectName("button_update_event")
        self.button_menu = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu.setGeometry(QtCore.QRect(90, 420, 171, 51))
        self.button_menu.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu.setObjectName("button_menu")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(150, 110, 311, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(2)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 50 oblique 20 \"Cantarell\";\n"
"color: white")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 645, 25))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Atualizar bilhetes</p></body></html>"))
        self.label_cpf.setText(_translate("MainWindow", "<html><head/><body><p>Organizador-CPF</p></body></html>"))
        self.line_edit_cpf.setInputMask(_translate("MainWindow", "999.999.999.99"))
        self.label_data.setText(_translate("MainWindow", "<html><head/><body><p>Data</p></body></html>"))
        self.date_edit.setDisplayFormat(_translate("MainWindow", "d/M/yy"))
        self.label_ticket_number.setText(_translate("MainWindow", "Nº"))
        self.line_edit_id.setInputMask(_translate("MainWindow", "99999"))
        self.choose_type.setItemText(0, _translate("MainWindow", "Adicionar"))
        self.choose_type.setItemText(1, _translate("MainWindow", "Remover"))
        self.button_update_event.setText(_translate("MainWindow", "Efetuar"))
        self.button_menu.setText(_translate("MainWindow", "Voltar aos serviços"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Atualizações:</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

