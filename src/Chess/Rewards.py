import chess

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
MISSIONS = []
M_FLAGS = [0, 0, 0, 0]

"""
Make a function which calls all the mission check functions together and add the function call to analyse move 
Once a mission is completed, set the corresponding flag to 1 

add a function which goes through all the flags after every move and alerts the GUI if a flag is 1 
"""


"""
CHECK MOVE PERFORMANCE (MISSIONS MIGHT BE COMPLETED IN GIVEN MOVE)
IF @check is True THEN IS HELPS AI TO CHECK IF MOVE GENERATES A VICTIM
"""
def analyzeMove(board, player_id, move, check=False):
    victim = None
    kill_vic = check_victim(board, move)
    if is_victim(kill_vic):
        killer = str(kill_vic[0]).lower()
        victim = str(kill_vic[1]).lower()
        if not check:
            victims.get(player_id).append(dic.get(victim))
            for mission_id in range(0, len(MISSIONS)):
                check_kill_vic_pairs(killer, victim, player_id, mission_id)
                check_pawns(player_id, mission_id)
                #check_pawns_killed_mission(player_id)
    """REMOVE THIS LINE IT IS JUST FOR TESTING"""
    if not check:
        print(victims)
    return victim


"""CHECK IF THERE IS A VICTIM"""
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


def check_one_kill(player_id, mission_id):
    if MISSIONS[mission_id] in ['Kill 1 bishop', 'Kill 1 knight', 'Kill 1 rook']:
        bishop = victims.get(player_id).count('bishop')
        knight = victims.get(player_id).count('knight')
        rook = victims.get(player_id).count('rook')
        if bishop == 1 or knight == 1 or rook == 1:
            print(f'Mission {MISSIONS[mission_id]} completed by player {player_id}')
            MISSIONS[mission_id] = 'COMPLETED'


"""CHECK COUNT PAWN MISSIONS EITHER 2 OR 4 PAWNS"""
def check_pawns(player_id, mission_id):
    pawns_killed = victims.get(player_id).count("pawn")
    if MISSIONS[mission_id] == 'Kill 2 pawns in a single game':
        if pawns_killed == 2:
            print(f'Mission {MISSIONS[mission_id]} completed by player {player_id}')
            MISSIONS[mission_id] = 'COMPLETED'
    elif MISSIONS[mission_id] == 'Kill 4 pawns in a single match':
        if pawns_killed == 4:
            print(f'Mission {MISSIONS[mission_id]} completed by player {player_id}')
            MISSIONS[mission_id] = 'COMPLETED'

"""
CHECK KILLER-VICTIM MISSIONS BY A GIVEN PLAYER
"""
def check_kill_vic_pairs(killer, victim, player_id, mission_id):
    if kill_vic_pairs.__contains__((killer, victim)):
        KILLER = dic.get(killer)
        VICTIM = dic.get(victim)
        string = str(MISSIONS[mission_id])
        l = string.split(' ')
        try:
            l.pop(l.index(KILLER))
            l.pop(l.index(VICTIM))
            print(f'mission completed - {string} by player {player_id}')
            MISSIONS[mission_id] = 'COMPLETED'
            M_FLAGS[mission_id] = 1
            print(M_FLAGS)
            print(MISSIONS)
            return
        except ValueError:
            return

def check_pawns_killed_mission(player_id):
    pawns = victims.get(player_id).count('pawn')
    if pawns == 2:
        print(f'Mission')

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


"""
SET MISSIONS GLOBALLY FOR BOTH PLAYERS
"""
def set_missions(m):
    global MISSIONS
    MISSIONS = m

    # if m =4 and board is checkmate
    # mission gets accomplished

#   for i in range(0,no_of_victims):
#     if ((victims.get(player))[i] == "PAWN") :
