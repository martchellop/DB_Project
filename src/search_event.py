from PyQt5 import QtWidgets
from autoSearchEvent import Ui_MainWindow

import queries
import main_screen
import utils


class searchScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(searchScreen, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect buttons
        self.ui.button_search_events.clicked.connect(self.handle_search_events)
        self.ui.button_menu.clicked.connect(self.handle_menu)

    # Handles
    def handle_menu(self):
        self.anotherwindow = main_screen.MainScreen()
        self.anotherwindow.show()
        self.bypass = True
        self.close()
        return


    def handle_search_events(self):
        event_type = str(self.ui.combo_box_choose_event_type.currentText())
        date_start = self.ui.date_edit_start.date().toPyDate()
        date_end = self.ui.date_edit_end.date().toPyDate()
        organizer_cpf = self.ui.line_edit_cpf.text()

        # Deals with empty cpf or invalid amount of digits
        if organizer_cpf == "...":
            organizer_cpf = None
        elif len(organizer_cpf) != 14:
            utils.warning("CPF inválido!")
            return

        organizer_name = self.ui.line_edit_name.text()
        if not organizer_name:
            organizer_name = None

        model = queries.search_events(event_type, date_start, date_end,
                                      organizer_cpf, organizer_name)
        if model:
            self.ui.table_search_results.setModel(model)
        else:
            utils.warning("Nenhuma festa com esses parâmetros encontrada!")

    # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = searchScreen()
    GUI.show()
    sys.exit(APP.exec_())
