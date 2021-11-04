import chess
import pygame.display
import sys
import Missions
import Rewards

from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Rewards

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

def start(window,playerId, missions):
    turn = 0
    count = 0
    player2 = PLAYERS[playerId]
    # Rewards.setMissions(player1)
    # Rewards.setMissions(player2)
    while not board.is_checkmate():
        Board.draw_board(board.fen(), window)
        pygame.display.update()
        time.sleep(2)
        player = turn % 2
        if player == 0:
            move = player1.makeMove(board)
            while move is None:
                move = player1.makeMove(board)
            Rewards.analyzeMove(board, player, move)
            count = count + 1
            Rewards.count_moves(count, board)
            board.push(move)
            turn += 1
        else:
            m = player2.makeMove(board)
            Rewards.analyzeMove(board, player, m)
            board.push(m)
            turn += 1
        print(board)
        # move = ("".join(voice.getMove().split(" "))).lower()

# start(screen,1)
