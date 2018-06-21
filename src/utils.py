from PyQt5 import QtWidgets

def warning(message):
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
def closeEvent(bypass, event):
    # Verifies if the user wants to exit the window
    if bypass:
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
