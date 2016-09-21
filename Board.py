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
        self.playerPieces = []
        self.aiPieces = []
        self.allPieces = []
        self.pieces = 0

    def __repr__(self):
        board = ''
        for i in range(self.BoardHeight):
            board = board + str(self.board[i]) + '\n'
        return board

    def __getitem__(self, key):
        return self.board[key]

    def update(self):
        for i in range(len(self.board)):
            for ii in range(len(self.board[i])):
                if (self.board[i][ii] == -1):
                    self.squares[str(i)+","+str(ii)].setPlayer1()
                elif (self.board[i][ii] == 1):
                    self.squares[str(i)+","+str(ii)].setPlayer2()

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
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m-1][n] == 0):
                self.allPieces.append(self.squares[str(m-1)+","+str(n)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m+1][n] == 0):
                self.allPieces.append(self.squares[str(m+1)+","+str(n)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and  self.board[m][n+1] == 0):
                self.allPieces.append(self.squares[str(m)+","+str(n+1)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m][n-1] == 0):
                self.allPieces.append(self.squares[str(m)+","+str(n-1)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m+1][n+1] == 0):
                self.allPieces.append(self.squares[str(m+1)+","+str(n+1)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m+1][n-1] == 0):
                self.allPieces.append(self.squares[str(m+1)+","+str(n-1)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m-1][n-1] == 0):
                self.allPieces.append(self.squares[str(m-1)+","+str(n-1)])
        if (m - 1 >= 0 and n - 1 and m + 1 <= 14 and n + 1 <= 14 and self.board[m-1][n+1] == 0):
                self.allPieces.append(self.squares[str(m-1)+","+str(n+1)])
        print(self)
        print(self.allPieces)

        return self.allPieces.copy()

    def checkWin(self, m, n, player):

        count = 1
        self.pieces = self.pieces + 1
        if (self.pieces == 15 * 15):
            return DRAW

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.board[m - i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.board[m + i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.board[m - i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.board[m + i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.board[m][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.board[m][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.board[m + i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.board[m - i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        return CONTINUE
