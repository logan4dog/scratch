# Structure of PyQt5 GUIs

# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 

class GUI(QMainWindow):    # Inherit from QMainWindow
    def __init__(self):
        super().__init__() # Init super class, it creates window

        self.initUI()

    def initUI(self):    # Set properites and add widgets
        self.setWindowTitle("PyQt5 Boiler Plate") # Add widgets and change properties
        self.resize(400,500)
        self.statusBar().showMessage('Status message')

# Show the constructed PyQt window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
# execute the application
    sys.exit(app.exec_())

