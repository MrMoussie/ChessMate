import chess
from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Update
import Rewards
#from src.GUI import board as BOARD

window = None


# init Board
board = chess.Board()

# set Players
player1 = Player("Joe")
player2 = Naive('s')
#player2 = Smart('Smart')

# start game

print(board)
print(board.fen())

screen = None
BOARD = None

def start():
    turn = 0
    while not board.is_checkmate():
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
        print(str(board.fen()))
        #Update.update(str(board.fen()))
        BOARD.draw_board(board.fen(), window)
        print(board)
        ##move = ("".join(voice.getMove().split(" "))).lower()


def play(window_surface):
    window = window_surface
    start()

def setup(window, board):
    global screen
    screen = window
    global BOARD
    BOARD = board
