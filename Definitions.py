from enum import Enum, unique

@unique
class Direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL_ASCENDING = 3
    DIAGONAL_DESCENDING = 4

@unique
class Player(Enum):
    MAX = 1
    MIN = 2

@unique
class GameType(Enum):
    PvP = 1  # Player versus Player
    PvE = 2  # Player versus Environment (the IA)

@unique
class StoneType(Enum):
    BLANK = 0
    BLACK = 1
    WHITE = 2

@unique
class GameState(Enum):
    WIN = 0
    DRAW = 1
    RUNNING = 2