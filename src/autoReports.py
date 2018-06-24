# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reports.ui'
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
        self.button_search_events = QtWidgets.QPushButton(self.centralWidget)
        self.button_search_events.setGeometry(QtCore.QRect(270, 550, 131, 51))
        self.button_search_events.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_search_events.setObjectName("button_search_events")
        self.table_search_results = QtWidgets.QTableView(self.centralWidget)
        self.table_search_results.setGeometry(QtCore.QRect(500, 100, 551, 631))
        self.table_search_results.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.table_search_results.setObjectName("table_search_results")
        self.button_menu = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu.setGeometry(QtCore.QRect(90, 550, 151, 51))
        self.button_menu.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu.setObjectName("button_menu")
        self.choose_report = QtWidgets.QComboBox(self.centralWidget)
        self.choose_report.setGeometry(QtCore.QRect(50, 150, 421, 81))
        self.choose_report.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.choose_report.setObjectName("choose_report")
        self.choose_report.addItem("")
        self.choose_report.addItem("")
        self.choose_report.addItem("")
        self.choose_report.addItem("")
        self.choose_report.addItem("")
        self.choose_report.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Relatórios</p></body></html>"))
        self.button_search_events.setText(_translate("MainWindow", "Pesquisar"))
        self.button_menu.setText(_translate("MainWindow", "Voltar ao menu"))
        self.choose_report.setItemText(0, _translate("MainWindow", "As festas que contrataram uma chácara"))
        self.choose_report.setItemText(1, _translate("MainWindow", "O custo médio das festas agrupado por tipo"))
        self.choose_report.setItemText(2, _translate("MainWindow", "A média e o desvio padrão do custo dos espaços alugados"))
        self.choose_report.setItemText(3, _translate("MainWindow", "A média do preço dos bilhetes que custam mais de 10"))
        self.choose_report.setItemText(4, _translate("MainWindow", "A média da quantidade de convidados de uma festa de casamento"))
        self.choose_report.setItemText(5, _translate("MainWindow", "As empresas que fornecem algum tipo de serviço para festa universitária"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

