import chess
import pygame.display
import sys
import Missions

from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Rewards

sys.path.append("../GUI")
#import board as Board
import time

# init Board
board = chess.Board()

# set Players
player1 = Player()
# player2 = Naive('s')
PLAYERS = [Player(), Naive(), Smart()]

# start game
Missions.current_mission_set()
print(board)
print(board.fen())

screen = None
BOARD = None


def start(window,playerId):
    turn = 0
    player2 = PLAYERS[playerId]
    while not board.is_checkmate():
        print("FEN:")
        print(board.fen())
        #Board.draw_board(board.fen(), window)
        #pygame.display.update()
        time.sleep(2)
        player = turn % 2
        if player == 0:
            move = player1.makeMove(board)
            while move is None:
                move = player1.makeMove(board)
            Rewards.analyzeMove(board, player, move)
            board.push(move)
            turn += 1
        else:
            m = player2.makeMove(board)
            Rewards.analyzeMove(board, player, m)
            board.push(m)
            turn += 1
        # BOARD.draw_board(board.fen(), window_surface)
        # print(str(board.fen()))
        # Update.update(str(board.fen()))
        # Board.draw_board(board.fen(), window)
        print(board)
        # move = ("".join(voice.getMove().split(" "))).lower()

start(screen,1)