import chess
class Player():
    def __init__(self,name):
        self.name = name
    
    def makeMove(self, board):
        move = input("Give me your move: ")
        Move = board.parse_uci(move)
        if board.is_legal(Move):
            return Move
        else: return None
    
