from PyQt5 import QtWidgets
from autoUpdateLocalization import Ui_MainWindow

import update_services
import queries
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

        # Connect type box to make price visible or not
        self.ui.choose_type.activated.connect(self.change_price_option)
        self.change_price_option()


    # Makes the price visible/invisible
    def change_price_option(self):
        option = self.ui.choose_type.currentText()

        # Make invisible
        if 'Adicionar' in option or 'Remover' in option:
            stylesheet = 'font: 14pt "Cantarell"; color: rgb(46, 52, 54);'
        else:
            stylesheet = 'font: 14pt "Cantarell"; color: white;'

        self.ui.text_price.setStyleSheet(stylesheet)
        self.ui.line_edit_price.setStyleSheet(stylesheet)
        self.ui.label_event_info.setStyleSheet(stylesheet)
        self.ui.label_cpf.setStyleSheet(stylesheet)
        self.ui.label_data.setStyleSheet(stylesheet)
        self.ui.line_edit_cpf.setStyleSheet(stylesheet)
        self.ui.date_edit.setStyleSheet(stylesheet)

    # Handles
    def handle_menu(self):
        self.anotherwindow = update_services.updateServices()
        self.anotherwindow.show()
        self.bypass = True
        self.close()
        return


    def handle_update_event(self):
        option = self.ui.choose_type.currentText()
        cep = self.ui.line_edit_cpf.text()

        # Deals with empty cpf or invalid amount of digits
        if cep == "-" or len(cep) != 9:
            utils.warning("cep inválido!")
            return

        if 'Adicionar' in option:
            message = queries.localization_service(cep, create=True)
        elif 'Remover' in option:
            message = queries.localization_service(cep, create=False)
        else:   # Update price
            date = self.ui.date_edit.date().toPyDate()
            organizer_cpf = self.ui.line_edit_cpf.text()
            price = self.ui.line_edit_price.text()
            if not price:
                utils.warning("Preço inválido")
                return
            price = int(price)

            # Deals with empty cpf or invalid amount of digits
            if organizer_cpf == "..." or len(organizer_cpf) != 14:
                utils.warning("CPF inválido!")
                return

            message = queries.update_localization_service(cep, price)
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
