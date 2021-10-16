import utils
import chess

class Player():
    def __init__(self,name):
        self.name = name
    
    def makeMove(self, board):
        move = input("Give me your move: ")
        checkMove = utils.isValid(move)
        if checkMove:
            print(checkMove)
            isLegal = board.is_legal(board.parse_uci(move))
            if isLegal:
                doMove = board.parse_uci(move)
            return doMove
        else: return None
    
