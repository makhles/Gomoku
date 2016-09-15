from PyQt4 import QtGui, QtCore
from Definitions import Player, GameState
from Game import Game
from Square import Square

class Board(QtGui.QFrame):
    playSignal = QtCore.pyqtSignal(Square.Square)
    width = 15
    height = 15

    def __init__(self, parent, game):
        super(Board, self).__init__(parent)
        self.game = game
        self.initBoard()

    def __getitem__(self, key):
        return self.board[key]

    def initBoard(self):
        self.occupiedTiles = []
        i = 0
        for n in range(self.height):
            ii = 0
            for m in range(self.width):
                square = Square.Square(self, n, m)
                square.setGeometry(ii, i, 40, 40)
                if ((m == 7 and n == 7) or
                    (m == 4 and n == 4) or (m == 4 and n == 10) or
                    (m == 10 and n == 4) or (m == 10 and n == 10)):
                    square.setNormal2()
                else:
                    square.setNormal()
                self.connect(square, QtCore.SIGNAL('clicked()'), self.onTileClicked)
                ii = ii + 40
            i = i + 40
        print(self.board)

    def onTileClicked(self):
        if self.game.state == GameState.RUNNING:
            self.tile = self.sender()
            if tile not in occupiedTiles
                self.occupiedTiles.add(tile)
                self.game.play()

    def update(self):
        if self.game.player == Player.MAX:
            self.tile.setBlackStone()
        else
            self.tile.setWhiteStone()
