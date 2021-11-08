import chess

"""MAPPING PIECES CHAR TO STRINGS"""
dic = {'p': 'pawn', 'n': 'knight',
       'k': 'king', 'q': 'queen',
       'b': 'bishop', 'r': 'rook'}

"""TRACKING VICTIMS OF PLAYERS"""
victims = {0: [], 1: []}
checks = {}


"""KILL-VICTIM PAIRS TO CHECK"""
kill_vic_pairs = [('p', 'p'), ('b', 'p'), ('r', 'p'), ('q', 'p'), ('n', 'p'), ('k', 'p'), ('p', 'p'), ('q', 'n'),
                  ('q', 'q'), ('n', 'n'), ('n', 'q'), ('r', 'r'), ('b', 'b')]

"""Players' Missions"""
MISSIONS = []
M_FLAGS = [0, 0, 0, 0]

"""Tracking number of moves of players"""
MOVES = {0: [0], 1: [0]}

"""
CHECK MOVE PERFORMANCE (MISSIONS MIGHT BE COMPLETED IN GIVEN MOVE)
IF @check is True THEN IS HELPS AI TO CHECK IF MOVE GENERATES A VICTIM
"""
def analyzeMove(board, player_id, move, alert_function, check=False):
    victim = None
    kill_vic = check_victim(board, move)
    if is_victim(kill_vic):
        killer = str(kill_vic[0]).lower()
        victim = str(kill_vic[1]).lower()
        if not check:
            victims.get(player_id).append(dic.get(victim))
            MOVES.get(player_id)[0] = MOVES.get(player_id)[0] + 1
            for mission_id in range(0, len(MISSIONS)):
                check_kill_vic_pairs(killer, victim, player_id, mission_id, alert_function)
                check_pawns(player_id, mission_id, alert_function)
                check_one_kill(player_id, mission_id, alert_function)
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


"""CHECK A PIECE WAS KILLED (bishop, knight, rook, pawn)"""
def check_one_kill(player_id, mission_id, alert_function):
    mission = MISSIONS[mission_id]
    string = str(mission)
    if mission in ['Kill 1 bishop', 'Kill 1 knight', 'Kill 1 rook']:
        print('now here')
        bishop = victims.get(player_id).count('bishop')
        knight = victims.get(player_id).count('knight')
        rook = victims.get(player_id).count('rook')
        if bishop == 1 or knight == 1 or rook == 1:
            alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
            MISSIONS[mission_id] = 'COMPLETED'
            print(MISSIONS)
    elif mission == 'Get 1 pawn killed within the first 6 moves':
        if victims.get(player_id).count('pawn') == 1 and MOVES.get(player_id)[0] <= 6:
            alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
            MISSIONS[mission_id] = 'COMPLETED'
            print(MISSIONS)


"""CHECK COUNT PAWN MISSIONS EITHER 2 OR 4 PAWNS"""
def check_pawns(player_id, mission_id, alert_function):
    pawns_killed = victims.get(player_id).count("pawn")
    string = str(MISSIONS[mission_id])
    if string == 'Kill 2 pawns in a single game':
        if pawns_killed == 2:
            alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
            MISSIONS[mission_id] = 'COMPLETED'
    elif string == 'Kill 4 pawns in a single match':
        if pawns_killed == 4:
            alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
            MISSIONS[mission_id] = 'COMPLETED'

"""
CHECK KILLER-VICTIM MISSIONS BY A GIVEN PLAYER
"""
def check_kill_vic_pairs(killer, victim, player_id, mission_id, alert_function):
    if kill_vic_pairs.__contains__((killer, victim)):
        KILLER = dic.get(killer)
        VICTIM = dic.get(victim)
        string = str(MISSIONS[mission_id])
        l = string.split(' ')
        try:
            l.pop(l.index(KILLER))
            l.pop(l.index(VICTIM))
            alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
            MISSIONS[mission_id] = 'COMPLETED'
            M_FLAGS[mission_id] = 1
            print(M_FLAGS)
            print(MISSIONS)
            return
        except ValueError:
            return

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