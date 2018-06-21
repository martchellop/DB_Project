from PyQt5 import QtWidgets
from autoUpdateEvent import Ui_MainWindow

import queries
import main_screen

class updateScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(updateScreen, self).__init__()
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
            self.warning("CPF inválido!")
            return

        # Deals with the user not selecting anything to be changed
        if not self.ui.check_date.isChecked() and not self.ui.check_cpf.isChecked():
            self.warning("Nada selecionado para ser atualizado!")
            return

        message = queries.update_uni_event(date, organizer_cpf, new_date, new_cpf)
        self.warning(message)


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
    GUI = updateScreen()
    GUI.show()
    sys.exit(APP.exec_())
