from PyQt5 import QtWidgets
from autoMainWindow import Ui_MainWindow

import reports
import create_event
import update_event
import search_event
import update_services

import queries
import utils

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect general buttons
        self.ui.button_search_events.clicked.connect(self.handle_search_events)
        self.ui.button_reports.clicked.connect(self.handle_reports)

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
        utils.warning("O sistema parece estar fora do ar, por favor tentar mais tarde")

    def handle_uni_create(self):
        self.change_windows(create_event.createScreen())

    def handle_uni_update(self):
        self.change_windows(update_event.updateScreen())

    def handle_uni_services(self):
        self.change_windows(update_services.updateServices())

    def handle_search_events(self):
        self.change_windows(search_event.searchScreen())

    def handle_reports(self):
        self.change_windows(reports.reports())


    def change_windows(self, new_window):
        self.anotherwindow = new_window
        self.anotherwindow.show()
        self.bypass = True
        self.close()


    # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)
        return

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = MainScreen()
    GUI.show()
    sys.exit(APP.exec_())
