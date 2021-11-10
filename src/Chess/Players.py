import chess, Leaderboard

import utils
import voice
import re




def analyze_promotion(board, move):
    try:
        move_san = board.san(chess.Move.from_uci(move))
        moves = ' '.join(re.sub("[(,<>)]", "", str(board.legal_moves)).split(" ")[3:])
        print('is in the list', moves.__contains__(move_san))
        return moves.__contains__(move_san)
    except ValueError and AssertionError:
        return False
    except ValueError:
        return False
    except AssertionError:
        return False



class Player:
    elo = 0
    def __init__(self):
        self.name = 'opponent'
        self.elo = Leaderboard.getElo(self.name)

    def set_elo(self, amount):
        self.elo = amount
        Leaderboard.updateElo(self.name, self.elo)

    def get_elo(self):
        return self.elo

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def makeMove(self, board):
        move = input("Give me your move: ")
        # move = voice.getmove("Give your move " + self.name)
        # print(move)
        checkMove = utils.isValid(move)
        if checkMove:
            print('pseudo moves ', board.pseudo_legal_moves)
            try:
                isLegal = board.is_pseudo_legal(board.parse_uci(move))
                doMove = None
                print('it is legal', isLegal)
                if isLegal:
                    doMove = board.parse_san(move)
            except ValueError:
                print('VALUE ERROR')
                promotion = analyze_promotion(board, move)
                doMove = None
                if promotion:
                    print('will be promoted')
                    add = self.take_promotion()
                    while add is None:
                        add = self.take_promotion()
                    doMove = board.san(chess.Move.from_uci(move))
                    print('promoting', doMove + '='+add)
                    doMove = board.parse_san(str(move + '='+add))
                    print('doMove', doMove)
                return doMove
            except AssertionError:
                print('ASSERTION ERROR')
                return
            return doMove
        else:
            return

    def take_promotion(self):
        move = voice.getmove("THIS IS PROMOTION " + self.name, promotion=True)
        print('taking promotion', move)
        return move
