import Rewards
import re
import random


class Naive:

    def __init__(self):
        self.name = 'Naive'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    """RETURNS A VALID MOVE"""
    def makeMove(self, board):
        moves = re.sub("[(,<>)]", "", str(board.legal_moves)).split(" ")[3:]
        return board.parse_san(random.choice(moves))


class Smart:
    def __init__(self):
        self.name = 'Smart'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def makeMove(self, board):
        moves = re.sub("[(,<>)]", "", str(board.legal_moves)).split(" ")[3:]
        for move in moves:
            killer, victim, castling, check = Rewards.analyzeMove(board, board.parse_san(move))
            if victim is not None:
                return board.parse_san(move)
        return board.parse_san(random.choice(moves))


class AI:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def makeMove(self, board):
        moves = re.sub("[(,<>)]", "", str(board.legal_moves)).split(" ")[3:]
        return board.parse_san(random.choice(moves))
