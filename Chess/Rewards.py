import chess

dic = {'p': 'PAWN', 'n': 'KNIGHT',
       'k': 'KING', 'q': 'QUEEN',
       'b': 'BISHOP', 'r': 'ROOK'}
victims = {0: [], 1: []}
checks = {}
pawns_killed = 0


def analyzeMove(board, player, move):
    move = move.uci()
    src = move[0:2]
    dst = move[2:]
    squareSrc = chess.parse_square(src)
    squareDst = chess.parse_square(dst)
    killer = board.remove_piece_at(squareSrc)
    victim = board.remove_piece_at(squareDst)
    board.set_piece_at(squareSrc, killer)
    board.set_piece_at(squareDst, victim)
    # print(piece)
    if (victim is not None):
        victims.get(player).append(dic.get(str(victim).lower()))
        #check_victims(player)
    print(victims)
    return victim
def check_victims(player):
#print(no_of_victims)
    pawns_killed = (victims.get(player)).count("PAWN")
    print(pawns_killed)
    




#   for i in range(0,no_of_victims):
#     if ((victims.get(player))[i] == "PAWN") :
