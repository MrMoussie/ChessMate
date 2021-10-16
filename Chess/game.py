import chess
import voice
import re
from Players import Player
from ComputerPlayer import Naive
board = chess.Board()
player1 = Player("Joe")
player2 = Naive('s')
turn = 0



while board.is_checkmate()==False:
    if (turn%2)==0:
        mv1 = player1.makeMove(board)
        print(mv1)
        while (mv1 is None):
          mv1 = player1.makeMove()
        board.push(mv1)
        turn+=1
    else:
        print('s')
        m = player2.makeMove(board)
        board.push(m)
        turn+=1
    print(board)
    ##move = ("".join(voice.getMove().split(" "))).lower()