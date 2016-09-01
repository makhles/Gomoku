import sys
import os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        self.windowBoard = BoardFrame(self)
        self.setCentralWidget(self.windowBoard)

        self.setWindowTitle('Gomoku')
        self.resize(600, 600)
        self.center()

        self.show()

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)

class Square(QtGui.QLabel):

    def __init__(self, parent, m, n):
        QtGui.QLabel.__init__(self, parent)
        self.name = 'Square[' + str(m) + '][' + str(n) + ']'
        self.m = m
        self.n = n

    def __repr__(self):
        return self.name

    ''' Sobrescrevendo função do QtGui.QLabel'''
    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))

    def getCoord(self):
        return self.m, self.n

class Board():
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self):
        self.board = [[0 for i in range(self.BoardWidth)] for ii in range(self.BoardHeight)]

    def __repr__(self):
        board = ''
        for i in range(self.BoardHeight):
            board = board + str(self.board[i]) + '\n'
        return board

    def alterBoard(self, m, n, player):
        self.board[m][n] = player
        win = self.checkWin(m, n, player)
        print(self)
        return win

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

class BoardFrame(QtGui.QFrame):
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self, parent):
        super(BoardFrame, self).__init__(parent)
        self.board = Board()
        self.initBoard()
        self.player = 1


    def initBoard(self):
        n = 0
        for i in range(self.BoardHeight):
            m = 0
            for ii in range(self.BoardWidth):
                square = Square(self, i, ii)
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

def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
