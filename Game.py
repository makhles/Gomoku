from PyQt4 import QtGui
from copy import deepcopy, copy
import Board
import sys
import Window
import math
from sys import maxsize
INF = maxsize

WIN = 'w'
DRAW = 'd'
CONTINUE = 'c'

class Node(object):
    def __init__(self, depth, player, state, value = 0):
        self.depth = depth
        self.player = player
        self.state = state
        self.value = value
        self.children = []
        self.createChildren()

    def createChildren(self):
        if (self.depth < 0):
            print("+++++++++++=")
            print("Retorna")
            print("+++++++++++=")
            sys.exit(0)
            return
        print("--------------------")
        print("CHILDREN CREATION")
        print("--------------------")
        print(self.state)
        print(self.value)
        for i in self.state.squares.values():
            print("===========")
            print(i)
            print("===========")
            new_state = Board.Board()
            new_state.board = self.state.board.copy()
            new_state.squares = self.state.squares.copy()
            new_state.squares = new_state.alterBoard(i.m, i.n, self.player)
            self.children.append(Node(self.depth - 1, -self.player, new_state, self.realValue(i)))

        # if (self.depth < 0):
        #     return
        # for ii,i in self.state.squares.items():
        #     new_state = Board.Board()
        #     new_state.squares = self.state.squares.copy()
        #     new_state.board = self.state.board.copy()
        #     new_state.alterBoard(i.m, i.n, self.player)
        #     self.children.append(Node(self.depth - 1, -self.player, new_state, self.realValue(i)))

    def realValue(self, i):

        # return i

        points = {}
        attack = 0
        m = i.m
        n = i.n
        player = self.player

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.state[m - i][n - i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m - i >= 0 and n - i >= 0 and self.state[m - i][n - i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["DiagonalCE"] = attack
        attack = 0

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.state[m + i][n - i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m + i <= 14 and n - i >= 0 and self.state[m + i][n - i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["DiagonalBE"] = attack
        attack = 0

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.state[m - i][n + i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m - i >= 0 and n + i <= 14 and self.state[m - i][n + i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["DiagonalCD"] = attack
        attack = 0

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.state[m + i][n + i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m + i <= 14 and n + i <= 14 and self.state[m + i][n + i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["DiagonalBD"] = attack
        attack = 0

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.state[m][n + i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (n + i <= 14 and self.state[m][n + i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["Direita"] = attack
        attack = 0

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.state[m][n - i] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (n - i >= 0 and self.state[m][n - i] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["Esquerda"] = attack
        attack = 0

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.state[m + i][n] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m + i <= 14 and self.state[m + i][n] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                break
        points["Baixo"] = attack
        attack = 0

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.state[m - i][n] == player):
                attack = math.pow(attack, 5-i) + 10
            elif (m - i >= 0 and self.state[m - i][n] == 0):
                attack = math.pow(attack, 5-i) + 5
            else:
                attack = 0
                break
        points["Cima"] = attack
        attack = 0

        maxPoint = 0
        for strategy,point in points.items():
            if point > maxPoint:
                maxPoint = point

        return maxPoint



class Game(object):

    def __init__(self):
        self.player = -1
        self.pieces = 0

    def startGame(self):
        app = QtGui.QApplication(sys.argv)
        self.window = Window.Window()
        self.window.windowBoard.playSignal.connect(self.play)
        self.window.windowBoard = self.window.windowBoard
        self.emptySpaces = self.window.windowBoard.squares
        sys.exit(app.exec_())

    def play(self, sender):
        win = 0
        if self.player == -1:
            if(self.window.windowBoard[sender.m][sender.n] == 0):
                self.emptySpaces = self.window.windowBoard.alterBoard(sender.m, sender.n, self.player)
                sender.setPlayer1()
                win = self.checkWin(sender.m, sender.n, self.player)
                self.wonMesage(win)
                self.changePlayer()
                node = Node(2, self.player, self.window.windowBoard)
                sys.exit(0)
                i_bestValue = -self.player * INF
                for i in range(len(node.children)):
                    n_children = node.children[i]
                    val = minMax(n_children, 2, self.player)
                    if abs(self.player * INF - val) <= abs(self.player * INF - i_bestValue):
                        i_bestValue = val
                        bestChoice = i
                        print(bestChoice)
                        print(i_bestValue)
        # self.wonMesage(win)
        self.changePlayer()

    def minMax(node, depth, player):
        if (depth == 0) or (abs(node.value) == INF):
            return node.value

        bestValue = INF * -player
        print(node.value)

        for child in node.children:
            val = minMax(child, depth-1, -player)
            if (abs(INF * player - val) < abs(INF*player-bestValue)):
                bestValue = val

        return bestValue
    def AIplay(self):
        playData = [None, None, 0]
        playData[0].setPlayer2()
        self.window.windowBoard.alterBoard(playData[0].m, playData[0].n, self.player)
        win = self.checkWin(playData[0].m, playData[0].n, self.player)
        print(playData)
        return win

    def changePlayer(self):
        if (self.player == -1):
            self.player = 1
        else:
            self.player = -1

    def checkWin(self, m, n, player):

        count = 1
        self.pieces = self.pieces + 1
        if (self.pieces == 15 * 15):
            return DRAW

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.window.windowBoard[m - i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.window.windowBoard[m + i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.window.windowBoard[m - i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.window.windowBoard[m + i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.window.windowBoard[m][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.window.windowBoard[m][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.window.windowBoard[m + i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.window.windowBoard[m - i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        return CONTINUE


    def wonMesage(self, win):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)

        if win == 'w':

            msg.setText("Vencedor:  " + str(self.player) + "    ")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()
        if win == 'd':
            msg.setText("Empate")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()



def main():
    Game().startGame()

if __name__ == "__main__":
    main()
