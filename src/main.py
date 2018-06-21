import sys
from PyQt5 import QtWidgets
from main_screen import MainScreen


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    GUI = MainScreen()
    GUI.show()
    sys.exit(APP.exec_())
