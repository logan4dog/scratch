# Structure of PyQt5 GUIs

# Imports
import sys
from PyQt5.QtWidgets import QApplication
from mygui import GUI

# Show the constructed PyQt window
if __name__ == "__main__":
    app = 0
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
# execute the application
    sys.exit(app.exec_())

