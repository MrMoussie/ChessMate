import chess
from Players import Player
from ComputerPlayer import Naive
from ComputerPlayer import Smart
import Rewards


#init Board
board = chess.Board()

#set Players
player1 = Player("Joe")
player2 = Naive('s')
player2 = Smart('Smart')

#start game
turn = 0
print(board)
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
    print(board)
    ##move = ("".join(voice.getMove().split(" "))).lower()