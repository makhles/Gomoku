import sys
import os
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        player = 1

        self.tboard = Board(self, player)
        self.setCentralWidget(self.tboard)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        self.resize(600, 600)
        self.center()
        self.setWindowTitle('Gomoku')

        self.show()

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)

class ExtendedQLabel(QtGui.QLabel):

    def __init__(self, parent, m, n):
        QtGui.QLabel.__init__(self, parent)
        self.m = m
        self.n = n
        self.name = 'square_' + str(self.m) + '_' + str(self.n)

    def __repr__(self):
        return self.name

    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))

    def alterBoard(self, board, player):
        board.board[self.m][self.n] = player
        win = board.checkWin(self.m, self.n, player)
        print(board)
        return win

class BoardStructure():
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self):
        self.board = [[0 for i in range(self.BoardWidth)] for ii in range(self.BoardHeight)]

    def __repr__(self):
        board = ''
        for i in range(self.BoardHeight):
            board = board + str(self.board[i]) + '\n'
        return board

    def checkWin(self, m, n, player):
        print("Checking Win")
        count = 1

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.board[m - i][n - i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.board[m + i][n - i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.board[m - i][n + i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.board[m + i][n + i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.board[m][n + i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.board[m][n - i] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.board[m + i][n] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.board[m - i][n] == player):
                count = count + 1
                print("Count: " + str(count))
            else:
                break
        if (count == 5):
            print("Win")
            return 1
        else:
            count = 1

        return 0

class Board(QtGui.QFrame):
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self, parent, player):
        super(Board, self).__init__(parent)
        self.board = BoardStructure()
        self.initBoard()
        self.player = player


    def initBoard(self):
        n = 0
        for i in range(self.BoardHeight):
            m = 0
            for ii in range(self.BoardWidth):
                square = ExtendedQLabel(self, i, ii)
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
                win = self.sender().alterBoard(self.board, self.player)
                self.player = 2
        else:
            if(self.board.board[self.sender().m][self.sender().n] == 0):
                self.sender().setPixmap(QtGui.QPixmap(os.getcwd() + "/BoardSquareP2.png"))
                win = self.sender().alterBoard(self.board, self.player)
                self.player = 1
        if win == 1:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Warning)

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

            msg.setText("Vencedor:  " + str(self.player))
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
