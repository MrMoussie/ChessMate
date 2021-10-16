import chess
import voice
import re
from Players import Player
from ComputerPlayer import Naive
import Rewards
board = chess.Board()
player1 = Player("Joe")
player2 = Naive('s')
turn = 0

while not board.is_checkmate():
    if (turn%2)==0:
        mv1 = player1.makeMove(board)
        while (mv1 is None):
          mv1 = player1.makeMove()
        Rewards.kill2pawns(board, mv1)
        board.push(mv1)

        turn+=1

    else:
        m = player2.makeMove(board)
        board.push(m)
        turn+=1
    print(board)
    ##move = ("".join(voice.getMove().split(" "))).lower()