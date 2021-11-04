import chess
import Missions

"""MAPPING PIECES CHAR TO STRINGS"""
dic = {'p': 'pawn', 'n': 'knight',
       'k': 'king', 'q': 'queen',
       'b': 'bishop', 'r': 'rook'}

"""TRACKING VICTIMS OF PLAYERS"""
victims = {0: [], 1: []}
checks = {}

"""TRACKING NUMBER OF PIECES KILLED"""
pawns_killed = 0
knights_killed = 0
kings_killed = 0
queens_killed = 0
bishops_killed = 0
rooks_killed = 0

"""KILL-VICTIM PAIRS TO CHECK"""
kill_vic_pairs = [('p', 'p'), ('b', 'p'), ('r', 'p'), ('q', 'p'), ('n', 'p'), ('k', 'p'), ('p', 'p'), ('q', 'n'),
                  ('q', 'q'), ('n', 'n'), ('n', 'q'), ('r', 'r'), ('b', 'b')]


"""Players' Missions"""
missions = {0: [], 1: []}


"""
@ensures victims updated when killer kills a opponent's piece
"""



"""
Make a function which calls all the mission check functions together and add the function call to analyse move 
Once a mission is completed, set the corresponding flag to 1 

add a function which goes through all the flags after every move and alerts the GUI if a flag is 1 
"""
def analyzeMove(board, player_id, move):
    # print(piece)
    victim = None
    kill_vic = check_victim(board, move)
    if is_victim(kill_vic):
        killer = str(kill_vic[0]).lower()
        victim = str(kill_vic[1]).lower()
        victims.get(player_id).append(dic.get(victim))
        check_pawns(player_id)
        if kill_vic_pairs.__contains__((killer, victim)):
            check_kill_vic_pairs(killer, victim)
    print(victims)
    return victim


def is_victim(tuple):
    if tuple[1] is not None:
        return True
    return False


"""CHECK WHICH PIECE KILLED WHICH"""
def check_victim(board, move):
    move = move.uci()  # convert move to string
    src = move[0:2]  # getting the source
    dst = move[2:]  # getting the destination
    squareSrc = chess.parse_square(src)
    squareDst = chess.parse_square(dst)
    killer = board.remove_piece_at(squareSrc)
    victim = board.remove_piece_at(squareDst)
    board.set_piece_at(squareSrc, killer)
    board.set_piece_at(squareDst, victim)
    return tuple((killer, victim))

def is_piece_killed():
    'Kill 1 bishop.' or 'Kill 1 knight.' or 'Kill 1 rook.'



def check_pawns(player):
    pawns_killed = (victims.get(player)).count("PAWN")
    print(pawns_killed)


def check_kill_vic_pairs(killer, victim):
    KILLER = dic.get(killer)
    VICTIM = dic.get(victim)
    easy = Missions.get_easy_mission()
    # medium = Missions.get_medium_mission()
    # hard = Missions.get_hard_mission()
    # expert = Missions.get_expert_mission()
    if KILLER in easy and VICTIM in easy:
        print("Mission accomplished - %s" % easy)
        # return easy                                                   Note - add the samne in the every step of if-else ladder and uncomment when database is conencted
    # elif KILLER.lower() in medium and VICTIM.lower() in medium:             Uncomment once databas is connected
    #    print("Mission accomplished - %s" % medium)
    # elif KILLER.lower() in hard and VICTIM.lower() in hard:
    #   print("Mission accomplished - %s" % hard)
    # elif KILLER.lower() in expert and VICTIM.lower() in expert:
    #   print("Mission accomplished - %s" % expert)


def count_moves(m, board):
    if m == 4 and board.is_checkmate():
        print("something")
    elif m <= 20 and board.is_checkmate():
        print("something")
    elif m <= 40 and board.is_checkmate():
        print("something")





    # if m =4 and board is checkmate
    # mission gets accomplished

#   for i in range(0,no_of_victims):
#     if ((victims.get(player))[i] == "PAWN") :
