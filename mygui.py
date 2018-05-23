#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:22:37 2017

@author: james
"""
from PyQt5.QtWidgets import  QMainWindow, QAction
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLabel, QPushButton

class GUI(QMainWindow):    # Inherit from QMainWindow
    def __init__(self):
        super().__init__() # Init super class, it creates window
        self.initUI()

    def initUI(self):    # Set properites and add widgets
        self.setWindowTitle("PyQt5 Boiler Plate") # Add widgets and change properties
        self.resize(400,500)
        self.statusBar().showMessage('Status message')
        self.add_menus_and_status()
        self.positional_layout()
        
    def positional_layout(self):
        print(self.menuBar().size())
        menbar_height = self.menuBar().height()
        print(menbar_height)
        label = QLabel('Our first Widget',self)
        label.resize(120,30)
        label.move(10,menbar_height)
        button = QPushButton('Click',self)
        button.move(label.width() + 25,label.height())
    def add_menus_and_status(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        exit_menu = menubar.addMenu('Edit')
        new_icon = QIcon('icons/file_new.ico')
        new_action = QAction(new_icon,'New',self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')
        file_menu.addSeparator()
        exit_icon = QIcon('icons/exit.ico')
        exit_action = QAction(exit_icon,'Exit',self)
        exit_action.setStatusTip('Exit App')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)
