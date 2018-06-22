# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 577)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 411, 41))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 130, 771, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.button_uni_create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_uni_create.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_uni_create.setObjectName("button_uni_create")
        self.verticalLayout_6.addWidget(self.button_uni_create)
        self.button_uni_update = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_uni_update.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_uni_update.setObjectName("button_uni_update")
        self.verticalLayout_6.addWidget(self.button_uni_update)
        self.button_uni_services = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_uni_services.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_uni_services.setObjectName("button_uni_services")
        self.verticalLayout_6.addWidget(self.button_uni_services)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.button_wed_create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_wed_create.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_wed_create.setObjectName("button_wed_create")
        self.verticalLayout_5.addWidget(self.button_wed_create)
        self.button_wed_update = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_wed_update.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_wed_update.setObjectName("button_wed_update")
        self.verticalLayout_5.addWidget(self.button_wed_update)
        self.button_wed_services = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_wed_services.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_wed_services.setObjectName("button_wed_services")
        self.verticalLayout_5.addWidget(self.button_wed_services)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.button_reports = QtWidgets.QPushButton(self.centralWidget)
        self.button_reports.setGeometry(QtCore.QRect(290, 460, 278, 33))
        self.button_reports.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_reports.setObjectName("button_reports")
        self.button_search_events = QtWidgets.QPushButton(self.centralWidget)
        self.button_search_events.setGeometry(QtCore.QRect(290, 420, 278, 33))
        self.button_search_events.setStyleSheet("font: 14pt \"Cantarell\";\n"
"color: white")
        self.button_search_events.setObjectName("button_search_events")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 311, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(2)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 50 oblique 20 \"Cantarell\";\n"
"color: white")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(480, 90, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(2)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 50 oblique 20 \"Cantarell\";\n"
"color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 867, 25))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>NomeDaEmpresa</p></body></html>"))
        self.button_uni_create.setText(_translate("MainWindow", "Cadastro de festa universitária"))
        self.button_uni_update.setText(_translate("MainWindow", "Atualização de festa universitária"))
        self.button_uni_services.setText(_translate("MainWindow", "Serviços das festas universitárias"))
        self.button_wed_create.setText(_translate("MainWindow", "Cadastro de festa de casamento"))
        self.button_wed_update.setText(_translate("MainWindow", "Atualização de festa de casamento"))
        self.button_wed_services.setText(_translate("MainWindow", "Serviços das festas de casamento"))
        self.button_reports.setText(_translate("MainWindow", "Relatórios"))
        self.button_search_events.setText(_translate("MainWindow", "Pesquisar festas"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Festas Universitárias</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Festas de Casamento</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

