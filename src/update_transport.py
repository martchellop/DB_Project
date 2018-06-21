from PyQt5 import QtWidgets
from autoUpdateLocalization import Ui_MainWindow

import queries
import main_screen
import utils

class updateLocalization(QtWidgets.QMainWindow):
    def __init__(self):
        super(updateLocalization, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect buttons
        self.ui.button_update_event.clicked.connect(self.handle_update_event)
        self.ui.button_menu.clicked.connect(self.handle_menu)

    # Handles
    def handle_menu(self):
        self.anotherwindow = main_screen.MainScreen()
        self.anotherwindow.show()
        self.bypass = True
        self.close()
        return


    def handle_update_event(self):
        date = self.ui.date_edit.date().toPyDate()
        organizer_cpf = self.ui.line_edit_cpf.text()
        new_date, new_cpf = None, None

        # Deals with empty cpf or invalid amount of digits
        if organizer_cpf == "..." or len(organizer_cpf) != 14:
            utils.warning("CPF inválido!")
            return

        message = queries.update_uni_event(date, organizer_cpf, new_date, new_cpf)
        utils.warning(message)

    # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)
        return

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = updateLocalization()
    GUI.show()
    sys.exit(APP.exec_())
