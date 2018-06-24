from PyQt5 import QtWidgets
from autoUpdateTickets import Ui_MainWindow

import update_services
import queries
import utils


class updateTickets(QtWidgets.QMainWindow):
    def __init__(self):
        super(updateTickets, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect buttons
        self.ui.button_update_event.clicked.connect(self.handle_update_event)
        self.ui.button_menu.clicked.connect(self.handle_menu)

        # Connect type box to make ticket number visible or not
        self.ui.choose_type.activated.connect(self.change_price_option)
        self.change_price_option()


    # Makes the ticker number visible/invisible
    def change_price_option(self):
        option = self.ui.choose_type.currentText()

        # Make invisible
        if 'Adicionar' in option:
            stylesheet = 'font: 14pt "Cantarell"; color: rgb(46, 52, 54);'
        else:
            stylesheet = 'font: 14pt "Cantarell"; color: white;'

        self.ui.label_ticket_number.setStyleSheet(stylesheet)
        self.ui.line_edit_id.setStyleSheet(stylesheet)


    # Handles
    def handle_menu(self):
        self.anotherwindow = update_services.updateServices()
        self.anotherwindow.show()
        self.bypass = True
        self.close()
        return


    def handle_update_event(self):
        date = self.ui.date_edit.date().toPyDate()
        organizer_cpf = self.ui.line_edit_cpf.text()
        option = self.ui.choose_type.currentText()
        ticket_id = self.ui.line_edit_id.text()

        # Deals with blank ticket number
        if not ticket_id and 'Adicionar' not in option:
            utils.warning("Número do ticket inválido!")
            return

        # Deals with empty cpf or invalid amount of digits
        if organizer_cpf == "..." or len(organizer_cpf) != 14:
            utils.warning("CPF inválido!")
            return

        if 'Adicionar' in option:
            message = queries.tickets_service(date, organizer_cpf)
        elif 'Remover' in option:
            message = queries.tickets_service(date, organizer_cpf, int(ticket_id))
        utils.warning(message)


    # Overloading classes
    def closeEvent(self, event):
        utils.closeEvent(self.bypass, event)
        return

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    GUI = updateTickets()
    GUI.show()
    sys.exit(APP.exec_())
