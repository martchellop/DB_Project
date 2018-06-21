# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateServices.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 403)
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
        self.button_menu = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu.setGeometry(QtCore.QRect(40, 220, 151, 51))
        self.button_menu.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu.setObjectName("button_menu")
        self.button_menu_2 = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu_2.setGeometry(QtCore.QRect(40, 140, 151, 51))
        self.button_menu_2.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu_2.setObjectName("button_menu_2")
        self.button_menu_3 = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu_3.setGeometry(QtCore.QRect(210, 140, 151, 51))
        self.button_menu_3.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu_3.setObjectName("button_menu_3")
        self.button_menu_4 = QtWidgets.QPushButton(self.centralWidget)
        self.button_menu_4.setGeometry(QtCore.QRect(380, 140, 151, 51))
        self.button_menu_4.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_menu_4.setObjectName("button_menu_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 561, 25))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Atualizar servicos universitários</p></body></html>"))
        self.button_menu.setText(_translate("MainWindow", "Voltar ao menu"))
        self.button_menu_2.setText(_translate("MainWindow", "Localização"))
        self.button_menu_3.setText(_translate("MainWindow", "Transporte"))
        self.button_menu_4.setText(_translate("MainWindow", "Bilhetes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

