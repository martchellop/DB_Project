from PyQt5 import QtWidgets
from autoUpdateServices import Ui_MainWindow

import queries
import main_screen

import update_localization
import update_transport
import update_tickets

import utils

class updateServices(QtWidgets.QMainWindow):
    def __init__(self):
        super(updateServices, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect buttons
        self.ui.button_menu.clicked.connect(lambda x: \
                self.handle_menu(main_screen.MainScreen))
        self.ui.button_localization.clicked.connect(lambda x: \
                self.handle_menu(update_localization.updateLocalization))
        """
        self.ui.button_transport.clicked.connect(lambda x: \
                self.handle_menu(main_screen.updateTransport))
        self.ui.button_tickets.clicked.connect(lambda x: \
                self.handle_menu(main_screen.updateTickets))
        """


    # Handles
    def handle_menu(self, window_func):
        self.anotherwindow = window_func()
        self.anotherwindow.show()
        self.bypass = True
        self.close()
        return

  # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)
        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = updateServices()
    GUI.show()
    sys.exit(APP.exec_())
