import sys
from PyQt4 import QtGui, QtCore
from Definitions import GameType
from Game import Game
from Board import Board

class Gomoku(QtGui.QMainWindow):

    def __init__(self):
        super(Gomoku, self).__init__()
        self.initUI()

    def initUI(self):
        # Exit action
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction('Play against computer', self.startNewGame(GameType.PvE))
        fileMenu.addAction('Play against player', self.startNewGame(GameType.PvP))
        fileMenu.addAction(exitAction)

        # Window properties
        self.setWindowTitle('Gomoku')
        self.resize(600, 600)
        self.center()
        self.show()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)

    def startNewGame(self, gameType):
        self.game = Game(gameType, self)
        self.board = Board(self, game)
        self.setCentralWidget(self.board)

    def update(self):
        self.board.update()

def main():
    app = QtGui.QApplication(sys.argv)
    Gomoku()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()