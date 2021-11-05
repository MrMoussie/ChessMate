import utils
import voice


class Player:
    def __init__(self):
        self.name = 'opponent'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def makeMove(self, board):
        move = input("Give me your move: ")
        #move = voice.getmove("Give your move " + self.name)
        #print(move)
        checkMove = utils.isValid(move)
        if checkMove:
            print("move is valid ", checkMove)
            print(board.legal_moves)
            try:
                isLegal = board.is_pseudo_legal(board.parse_uci(move))
                if isLegal:
                    doMove = board.parse_uci(move)
            except ValueError:
                return
            print('move donehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            return doMove
        else:
            return None
