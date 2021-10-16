import Players
import re
import random

class Naive():

    def __init__(self, name):
        self.name = name
        
    def makeMove(self, board):
        moves = re.sub("[(,<>)]","", str(board.legal_moves)).split(" ")[3:]
        return board.parse_san(random.choice(moves))
    
    
class Smart():
    def __init__(self, name):
        self.name = name
    def makeMove(self, board):
        moves = re.sub("[(,<>)]","", str(board.legal_moves)).split(" ")[3:]
        return board.parse_san(random.choice(moves))


class AI():
    def __init__(self, name):
        self.name = name
    def makeMove(self, board):
        moves = re.sub("[(,<>)]","", str(board.legal_moves)).split(" ")[3:]
        return board.parse_san(random.choice(moves))