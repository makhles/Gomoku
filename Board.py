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
