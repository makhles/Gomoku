import sys
from Definitions import GameState, GameType, Player
from PyQt4 import QtGui, QtCore

class Game(object):

    def __init__(self, gameType, userInterface):
        self.gameType = gameType
        self.userInterface = userInterface
        self.player = Player.MAX  # Player 1 is always the MAX
        self.state = GameState.RUNNING
        self.aiPieces = {}
        if self.gameType == GameType.PvE:
            self.evaluateHeuristic()

    def play(self, row, col):
        if (self.gameType == GameType.PvP or
                (self.gameType == GameType.PvE and self.player == Player.MIN)):
            self.state = self.checkWinner(row, col)
            if self.state == GameState.WIN or self.state == GameState.DRAW:
                self.printResult()
            else:
                self.player = Player.MAX
                self.userInterface.update()
                self.evaluateHeuristic()

    def checkWinner(self, row, col):
        #TODO (pegar da antiga Board)
        return GameState.RUNNING

    def evaluateHeuristic(self):
        # TODO
        self.userInterface.update()
        self.player = Player.MIN

    def printResult(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle("Game end")

        if self.state == GameState.WIN:
            msg.setText("Winner: " + str(self.player) + "    ")
        elif self.state == GameState.DRAW:
            msg.setText("Game is a draw!")

        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()

    def updateTurnPlayer(self):
        if self.player == Player.MAX:
            self.player = Player.MIN
        else:
            self.player = Player.MAX

    def getstate(self):
        return self.state

    def getplayer(self):
        return self.player