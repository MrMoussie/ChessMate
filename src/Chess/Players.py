import utils
import voice
import chess

class Player():
    def __init__(self,name):
        self.name = name
    
    def makeMove(self, board):
        #move = input("Give me your move: ")
        move = voice.getmove("Give your move " + self.name)
        print(move)
        checkMove = utils.isValid(move)
        if checkMove:
            print(checkMove)
            try:
                isLegal = board.is_legal(board.parse_uci(move))
                if isLegal:
                    doMove = board.parse_uci(move)
            except ValueError:
                return
            return doMove
        else: return None
    
