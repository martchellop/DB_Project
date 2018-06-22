from PyQt5 import QtWidgets
from autoReports import Ui_MainWindow

import queries
import main_screen
import utils


class reports(QtWidgets.QMainWindow):
    def __init__(self):
        super(reports, self).__init__()
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
        option = self.ui.choose_report.currentIndex()
        print(type(option))
        model = queries.reports(option)
        if model:
            self.ui.table_search_results.setModel(model)
        else:
            utils.warning("Relatório vazio!")

 
    # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = reports()
    GUI.show()
    sys.exit(APP.exec_())
