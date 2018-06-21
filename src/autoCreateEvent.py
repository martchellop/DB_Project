# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createEvent.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 707)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 411, 41))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 532, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_create_event = QtWidgets.QPushButton(self.centralWidget)
        self.button_create_event.setGeometry(QtCore.QRect(460, 550, 131, 51))
        self.button_create_event.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_create_event.setObjectName("button_create_event")
        self.button_menu = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu.setGeometry(QtCore.QRect(60, 550, 151, 51))
        self.button_menu.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu.setObjectName("button_menu")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 653, 25))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Cadastrar festa universitária</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Organizador-CPF</p></body></html>"))
        self.line_edit_cpf.setInputMask(_translate("MainWindow", "999.999.999.99"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Data</p></body></html>"))
        self.date_edit.setDisplayFormat(_translate("MainWindow", "d/M/yy"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Preço</p></body></html>"))
        self.button_create_event.setText(_translate("MainWindow", "Criar"))
        self.button_menu.setText(_translate("MainWindow", "Voltar ao menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

