from PyQt5 import QtWidgets
from autoMainWindow import Ui_MainWindow

import search_event
import create_event
import update_event

import queries

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect general buttons
        self.ui.button_search_events.clicked.connect(self.handle_search_events)

        # Connect university buttons
        self.ui.button_uni_create.clicked.connect(self.handle_uni_create)
        self.ui.button_uni_update.clicked.connect(self.handle_uni_update)
        self.ui.button_uni_services.clicked.connect(self.handle_uni_services)

        # Conect useless buttons
        self.ui.button_wed_create.clicked.connect(self.handle_not_implemented)
        self.ui.button_wed_update.clicked.connect(self.handle_not_implemented)
        self.ui.button_wed_services.clicked.connect(self.handle_not_implemented)


    # Handles
    def handle_not_implemented(self):
        self.warning("O sistema parece estar fora do ar, por favor tentar mais tarde")

    def handle_uni_create(self):
        self.change_windows(create_event.createScreen())

    def handle_uni_update(self):
        self.change_windows(update_event.updateScreen())

    def handle_uni_services(self):
        pass
        #self.change_windows(search_event.searchScreen())

    def handle_search_events(self):
        self.change_windows(search_event.searchScreen())


    def change_windows(self, new_window):
        self.anotherwindow = new_window
        self.anotherwindow.show()
        self.bypass = True
        self.close()


    def warning(self, message):
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle("Aviso")
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Yes)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Ok')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            box.close()


    # Overloading classes
    def closeEvent(self, event):
        # Verifies if the user wants to exit the window
        if self.bypass:
            event.accept()
            return
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Saindo!')
        box.setText('Tem certeza que quer sair?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Sim')
        button_no = box.button(QtWidgets.QMessageBox.No)
        button_no.setText('Não')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            event.accept()
        elif box.clickedButton() == button_no:
            event.ignore()

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = MainScreen()
    GUI.show()
    sys.exit(APP.exec_())
