class Stone():
    def __init__(self, colour, x, y):
        self._colour = colour
        self._x = x
        self._y = y
        self._neighbours = {}
    def add_stone(self, position, stone):
        self._neighbours[position] = stone  # position in ['N', 'S', 'E', 'W']
    def x(self):
        return self._x
    def y(self):
        return self._y
    def neighbour(self, position):
        return self._neighbours[position]
