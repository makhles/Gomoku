from PyQt4 import QtGui, QtCore
import Square

WIN = 'w'
DRAW = 'd'
CONTINUE = 'c'

class Board(QtGui.QFrame):
    playSignal = QtCore.pyqtSignal(Square.Square)
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self, parent=None):
        super(Board, self).__init__(parent)
        self.squares = {}

    def __repr__(self):
        board = ''
        for i in range(self.BoardHeight):
            board = board + str(self.board[i]) + '\n'
        return board

    def __getitem__(self, key):
        return self.board[key]

    def initBoard(self):
        self.board = [[0 for i in range(self.BoardWidth)] for ii in range(self.BoardHeight)]
        i = 0
        for n in range(self.BoardHeight):
            ii = 0
            for m in range(self.BoardWidth):
                square = Square.Square(self, n, m)
                self.squares[str(square.m)+","+str(square.n)] = square
                square.setGeometry(ii, i, 40, 40)
                if ((m == 7 and n == 7) or
                    (m == 4 and n == 4) or (m == 4 and n == 10) or
                    (m == 10 and n == 4) or (m == 10 and n == 10)):
                    square.setNormal2()
                else:
                    square.setNormal()
                self.connect(square, QtCore.SIGNAL('clicked()'), self.play)
                ii = ii + 40
            i = i + 40

    def play(self):
        self.playSignal.emit(self.sender())

    def alterBoard(self, m, n, player):
        self.board[m][n] = player
        del self.squares[str(m)+","+str(n)]
        print(self)
        return self.squares.copy()
