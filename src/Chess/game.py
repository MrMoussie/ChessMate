import chess
import pygame.display

from src.Chess.Players import Player
from src.Chess.ComputerPlayer import Naive
from src.Chess.ComputerPlayer import Smart
import src.Chess.Rewards as Rewards
import src.GUI.board as Board
import time

# init Board
board = chess.Board()

# set Players
player1 = Player("Joe")
# player2 = Naive('s')
player2 = Smart('Smart')

# start game

print(board)
print(board.fen())

screen = None
BOARD = None

def start(window):
    turn = 0
    while not board.is_checkmate():
        print("FEN:")
        print(board.fen())
        Board.draw_board(board.fen(), window)
        pygame.display.update()
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
        #BOARD.draw_board(board.fen(), window_surface)
        # print(str(board.fen()))
        #Update.update(str(board.fen()))
        # Board.draw_board(board.fen(), window)
        # print(board)
        ##move = ("".join(voice.getMove().split(" "))).lower()

