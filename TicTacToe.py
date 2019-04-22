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
        self.quitCounter = 0

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

    def restoreSettings(self):
        if self.createLogFile:
            self.logger.debug("Starting restoreSettings")
        if self.appSettings.contains('createLogFile'):
            self.createLogFile = self.appSettings.value('createLogFile')
        else:
            self.createLogFile = logFilenameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)
        if self.appSettings.contains("pickleFilename"):
            self.pickleFilename = self.appSettings.value('pickleFilename', type=str)
        else:
            self.pickleFilename = pickleFilenameDefault
            self.appSettings.setValue('pickleFilename', self.pickleFilename)

    def ticTacToe(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        end = False
        win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def cancelClickedHandler(self):
        self.close()

