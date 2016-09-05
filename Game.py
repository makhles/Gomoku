import sys
from PyQt4 import QtGui, QtCore
import Window

class Game(object):

    def __init__(self):
        self.player = 1

    def startGame(self):
        app = QtGui.QApplication(sys.argv)
        self.window = Window.Window()
        self.window.windowBoard.playSignal.connect(self.play)
        sys.exit(app.exec_())

    def play(self, sender):
        win = 0
        if self.player == 1:
            if(self.window.windowBoard[sender.m][sender.n] == 0):
                sender.setPlayer1()
                win = self.window.windowBoard.board.alterBoard(sender.m, sender.n, self.player)
                self.player = 2
        else:
            if(self.window.windowBoard[sender.m][sender.n] == 0):
                sender.setPlayer2()
                win = self.window.windowBoard.board.alterBoard(sender.m, sender.n, self.player)
                self.player = 1
        self.checkWin(win)

    def checkWin(self, win):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        
        if win == 1:

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

            msg.setText("Vencedor:  " + str(self.player) + "    ")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()
        if win == 2:
            msg.setText("Empate")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()

def main():
    Game().startGame()

if __name__ == "__main__":
    main()
