from PyQt4 import QtGui, QtCore
import Square
import Board
import os

class BoardFrame(QtGui.QFrame):
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self, parent):
        super(BoardFrame, self).__init__(parent)
        self.board = Board.Board()
        self.initBoard()
        self.player = 1


    def initBoard(self):
        n = 0
        for i in range(self.BoardHeight):
            m = 0
            for ii in range(self.BoardWidth):
                square = Square.Square(self, i, ii)
                square.setGeometry(m, n, 40, 40)
                square.setPixmap(QtGui.QPixmap(os.getcwd() + "/BoardSquareNormal.png"))
                self.connect(square, QtCore.SIGNAL('clicked()'), self.play)
                m = m + 40
            n = n + 40
        self.board


    def play(self):
        if self.player == 1:
            if(self.board.board[self.sender().m][self.sender().n] == 0):
                self.sender().setPixmap(QtGui.QPixmap(os.getcwd() + "/BoardSquareP1.png"))
                m, n = self.sender().getCoord()
                win = self.board.alterBoard(m, n, self.player)
                self.player = 2
        else:
            if(self.board.board[self.sender().m][self.sender().n] == 0):
                self.sender().setPixmap(QtGui.QPixmap(os.getcwd() + "/BoardSquareP2.png"))
                m, n = self.sender().getCoord()
                win = self.board.alterBoard(m, n, self.player)
                self.player = 1
        if win == 1:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Warning)

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

            msg.setText("Vencedor:  " + str(self.player) + "    ")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()
