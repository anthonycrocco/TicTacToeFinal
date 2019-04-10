#!/usr/bin/env python
__author__ = "Anthony Crocco"


import sys
import tictactoeResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load


logFilenameDefault = 'tictactoe.log'
pickleFilenameDefault = '.tictactoeSave.pl'


class Tictactoe(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = getLogger('crocco.tictactoe')
        self.appSettings = QSettings()
        self.quitCounter = 0;

        uic.loadUi('TicTacToe.ui', self)

        self.pickleFilename = pickleFilenameDefault

        self.restoreSettings()

        if path.exists(self.pickleFilename):
            pass
        else:
            self.restartGame()
        # placeholder

    def __str__(self):
        pass

    def updateUI(self):
        if self.createLogFile:
            self.logger.info()

    def restartGame(self):
        if self.createLogFile:
            self.logger.debug("Restarting game")
        self.wins = 0
        self.losses = 0

    def saveGame(self):
        if self.createLogFile:
            self.logger.debug("Saving game")
        saveItems = ()
        if self.appSettings.contains('pickleFilename'):
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename', type=str)), 'wb') as pickleFile:
                return load(pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def restoreGame(self):
        if self.appSettings.conatains('pickleFilename'):
            self.appSettings.value('pickleFilename', type=str)
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename', type=str)), 'rb') as pickleFile:
                return load(pickleFile)
        else:
            self.logger.critical('No pickle Filename')


