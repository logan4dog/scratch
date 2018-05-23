# Structure of PyQt5 GUIs

# Imports
import sys
from PyQt5.QtWidgets import *

class GUI():
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.win = QWidget()    # create Window
        self.win.setWindowTitle("PyQt5 Boiler Plate") # Add widgets and change properties

# Show the constructed PyQt window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.win.show()
# execute the application
    sys.exit(app.exec_())

