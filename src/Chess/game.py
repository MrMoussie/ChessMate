import chess
import sys
from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Rewards
import atexit


sys.path.append("../GUI")
import time

# init Board
board = chess.Board()

# set Players
player1 = Player()
# player2 = Naive('s')
PLAYERS = [Player(), Naive(), Smart()]

print(board)

MISSIONS = ['Eliminate all opponent pieces before the king in a single game', 'Promote a pawn', 'Give a check using a pawn',
            'Kill 2 pawns in a single game']

move1 = ['e2e4', 'e4e5', 'e5e6', 'e6f7', 'd1f3', 'f3g3']
move2 = ['a7a6', 'a6a5', 'a5a4', 'e8f7', 'f7g6', 'g6f6']
c = ['e2e4', 'f7f6', 'd1h5', 'g7g6', 'f2f4', 'a7a6', 'f4f5', 'a6a5', 'f5g6', 'a5a4', 'g6h7']

FEN = board.fen()
TURN = 'WHITE'

def set_new_fen(fen):
    global FEN
    FEN = fen

def get_new_fen():
    return FEN

def get_flags():
    return Rewards.get_flags()

def set_turn(turn):
    global TURN
    TURN = turn
    
def start(player_name2, player_id2, player_name1, missions, alert_function):
    turn = 0
    player1.set_name(player_name1)
    player2 = PLAYERS[player_id2]
    player2.set_name(player_name2)
    Rewards.set_missions(missions)
    player = 0
    Rewards.set_players(player_name1, player, player_name2, 1)
    while not board.is_game_over(claim_draw=True):
        print('checkmate', board.is_checkmate())
        time.sleep(2)
        player = turn % 2
        if player == 0:
            move = player1.makeMove(board)
            while move is None:
                move = player1.makeMove(board)
            is_promote = False
            if len(str(move)) > 4:
                is_promote = True
            killer, victim, castling, check = Rewards.analyzeMove(board, move, promote=is_promote)
            Rewards.do_missions(check, victim, killer, player, castling, alert_function, promoted=is_promote)
            board.push_san(str(move))
            turn += 1
        else:
            if player_id2 == 0:
                move = player2.makeMove(board)
                while move is None:
                    move = player2.makeMove(board)
                is_promote = False
                if len(str(move)) > 4:
                    is_promote = True
                killer, victim, castling, check = Rewards.analyzeMove(board, move, promote=is_promote)
                Rewards.do_missions(check, victim, killer, player, castling, alert_function, promoted=is_promote)
                board.push_san(str(move))
            else:
                move = player2.makeMove(board)
                board.push(move)
            turn += 1
        if TURN == 'WHITE':
            set_turn('BLACK')
        else:
            set_turn('WHITE')
        Rewards.give_check(player, board.is_check())  # sends a check checker to the opponent
        set_new_fen(board.fen())
        print(board)
    Rewards.end_game(player, alert_function)

def set_turn(turn):
    global TURN
    TURN = turn

def get_turn():
    return TURN
#start(0, 'Joe', MISSIONS, None)