import chess
import sys
import Missions
from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Rewards
import pygame

sys.path.append("../GUI")
import board as Board
import time

# init Board
board = chess.Board()

# set Players
player1 = Player()
# player2 = Naive('s')
PLAYERS = [Player(), Naive(), Smart()]

# start game
print(Missions.current_mission_set())
print(board)

screen = None
BOARD = None

MISSIONS = ['Eliminate all opponent pieces before the king in a single game', 'Promote a pawn', 'Give a check using a pawn',
            'Kill 2 pawns in a single game']

move1 = ['e2e4', 'e4e5', 'e5e6', 'e6f7', 'd1f3', 'f3g3']
move2 = ['a7a6', 'a6a5', 'a5a4', 'e8f7', 'f7g6', 'g6f6']
c = ['e2e4', 'f7f6', 'd1h5', 'g7g6', 'f2f4', 'a7a6', 'f4f5', 'a6a5', 'f5g6', 'a5a4', 'g6h7']


def start(window, player_id, missions, alert_function):
    turn = 0
    count = 0
    player2 = PLAYERS[player_id]
    Rewards.set_missions(missions)
    player = 0
    while not board.is_game_over(claim_draw=True):
        print(board.outcome())
        print('checkmate', board.is_checkmate())
        Board.draw_board(board.fen(), window)
        pygame.display.update()
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
            # count = count + 1
            # Rewards.count_moves(count, board)
            board.push_san(str(move))
            turn += 1
        else:
            if player_id == 0:
                move = player2.makeMove(board)
                while move is None:
                    move = player2.makeMove(board)
                is_promote = False
                if len(str(move)) > 4:
                    is_promote = True
                killer, victim, castling, check = Rewards.analyzeMove(board, move, promote=is_promote)
                Rewards.do_missions(check, victim, killer, player, castling, alert_function, promoted=is_promote)
                # count = count + 1
                # Rewards.count_moves(count, board)
                board.push_san(str(move))
            else:
                move = player2.makeMove(board)
                board.push(move)
            turn += 1
        Rewards.give_check(player, board.is_check())  # sends a check checker to the opponent
        print(board)
    Rewards.end_game(player, alert_function)

#start(screen, 0, MISSIONS, None)
