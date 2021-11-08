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

"""Tracking number of checks of players"""
CHECKS = {0: [0, 0], 1: [0, 0]}

"""Consecutive checks"""
CON = {0: [0], 1: [0]}

"""Tracking points"""
POINTS = {0: [0], 1: [0]}


"""
CHECK WHICH PIECE KILL WHICH
if there is no victim then victim = None
@return two variables first the killer and then the victim
"""
def analyzeMove(board, move, promote=False):
    victim = None
    kill_vic = check_victim(board, move, promote)
    killer = str(kill_vic[0]).lower()
    castling = kill_vic[2]
    check = kill_vic[3]
    if is_victim(kill_vic):
        victim = str(kill_vic[1]).lower()
    return killer, victim, castling, check


"""START CHECKING EVERY MISSION"""
def do_missions(check, victim, killer, player_id, castling, alert_function, promoted=False):
    if CHECKS.get(player_id)[1] == 1:
        CHECKS.get(player_id)[0] = CHECKS.get(player_id)[0] + 1
        CHECKS.get(player_id)[1] = 0
    if check:
        CON.get(player_id)[0] = CON.get(player_id)[0] + 1
    else:
        CON.get(player_id)[0] = 0
    if victim is not None:
        victims.get(player_id).append(dic.get(victim))
    MOVES.get(player_id)[0] = MOVES.get(player_id)[0] + 1 # Increment MOVES counter
    for mission_id in range(0, len(MISSIONS)):
        mission = MISSIONS[mission_id]
        if mission != 'COMPLETED':
            check_kill_vic_pairs(killer, victim, player_id, mission, mission_id, alert_function)
            check_pawns(player_id, mission, mission_id, alert_function)
            check_one_kill(player_id, mission, mission_id, alert_function)
            check_check_counter(player_id, mission, mission_id, alert_function)
            check_castling(castling, player_id, mission, mission_id, alert_function)
            check_consecutive_check(player_id, mission, mission_id, alert_function)
            check_check_pawn(check, killer, player_id, mission, mission_id, alert_function)
            check_only_king_on_board(player_id, mission, mission_id, alert_function)
            check_mission_promotion(player_id, promoted, alert_function)


def check_mission_promotion(player, promoted, alert_function):
    if promoted:
        mission = 'Promote a pawn'
        if mission in MISSIONS:
            mission_id = MISSIONS.index(mission)
            send_mission_completed(mission, player, mission_id, alert_function)
            update_points(mission_id, player)

def check_only_king_on_board(player_id, mission, mission_id, alert_function):
    if mission == 'Eliminate all opponent pieces before the king in a single game':
        print('Total victims ',victims.get(player_id), len(victims.get(player_id)))
        if len(victims.get(player_id)) == 15:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)

"""
##########################################################################################
##########################SETTING MISSIONS AND CHECKING THEM##############################
##########################################################################################
"""

"""
SET MISSIONS GLOBALLY FOR BOTH PLAYERS
"""
def set_missions(m):
    global MISSIONS
    MISSIONS = m


"""CHECK IF THERE IS A VICTIM"""
def is_victim(tuple):
    if tuple[1] is not None:
        return True
    return False


"""
SET CHECK FLAG TO OPPONENT CHECKS EVERYTIME PLAYER MAKE CHECK MOVE
"""
def give_check(player, check):
    if check:
        if player == 0:
            CHECKS.get(1)[1] = 1
        elif player == 1:
            CHECKS.get(0)[1] = 1


def end_game(player_id, alert_function):
    win_a_game = 'Win a game'
    win_a_game_twenty = 'Win a game within 20 moves'
    win_a_game_thirty = 'Win a game within 30 moves'
    win_a_game_forty = 'Win a game within 40 moves'
    if win_a_game in MISSIONS:
        end_game_within_moves(win_a_game, player_id, alert_function)
    elif win_a_game_forty in MISSIONS and MOVES.get(player_id)[0] <= 40:
        end_game_within_moves(win_a_game_forty, player_id, alert_function)
    if win_a_game_twenty in MISSIONS and MOVES.get(player_id)[0] <= 20:
        end_game_within_moves(win_a_game_twenty, player_id, alert_function)
    elif win_a_game_thirty in MISSIONS and MOVES.get(player_id)[0] <= 30:
        end_game_within_moves(win_a_game_thirty, player_id, alert_function)
    print(get_total_points(player_id))
    return


def end_game_within_moves(win_a_game_moves, player_id, alert_function):
    mission_id = MISSIONS.index(win_a_game_moves)
    send_mission_completed(win_a_game_moves, player_id, mission_id, alert_function)
    update_points(mission_id, player_id)

"""SEND MISSION TO GUI TO DISPLAY  IT ONCE IT'S DONE"""
def send_mission_completed(string, player_id, mission_id, alert_function):
    print(f'MISSION COMPLETED! {string} Good job Player {player_id}!')
    # alert_function("MISSION COMPLETED!", f'{string}', f"Good job Player {player_id}!")
    MISSIONS[mission_id] = 'COMPLETED'
    M_FLAGS[mission_id] = 1
    print(MISSIONS)

def update_points(factor, player):
    POINTS.get(player)[0] = POINTS.get(player)[0] + (factor*10 + 10)
    print(POINTS)


def check_castling(castling, player_id, mission, mission_id, alert_function):
    if mission == 'Perform castling' and castling:
        send_mission_completed(mission, player_id, mission_id, alert_function)
        update_points(mission_id, player_id)

"""CHECK WHICH PIECE KILLED WHICH"""
def check_victim(board, move, promoted = False):
    print('missions ', move)
    is_castling = board.is_castling(move)
    is_check = board.gives_check(move)
    move = move.uci()  # convert move to string
    if promoted:
        move = move[0:4]
    src = move[0:2]  # getting the source
    dst = move[2:]  # getting the destination
    squareSrc = chess.parse_square(src)
    squareDst = chess.parse_square(dst)
    killer = board.remove_piece_at(squareSrc)
    victim = board.remove_piece_at(squareDst)
    board.set_piece_at(squareSrc, killer)
    board.set_piece_at(squareDst, victim)
    return tuple((killer, victim, is_castling, is_check))

"""CHECK IF PAWN DOES CHECK"""
def check_check_pawn(check, killer, player_id, mission, mission_id, alert_function):
    if check and mission == 'Give a check using a pawn' and killer == 'p':
        send_mission_completed(mission,player_id, mission_id, alert_function)


def check_consecutive_check(player_id, mission, mission_id, alert_function):
    if mission == 'Give two consecutive checks' and CON.get(player_id)[0] == 2:
        send_mission_completed(mission, player_id, mission_id, alert_function)
        update_points(mission_id, player_id)

"""CHECK A PIECE WAS KILLED (bishop, knight, rook, pawn)"""
def check_one_kill(player_id, mission, mission_id, alert_function):
    bishop = victims.get(player_id).count('bishop')
    knight = victims.get(player_id).count('knight')
    rook = victims.get(player_id).count('rook')
    #EASY MISSIONS
    if mission in ['Kill 1 bishop', 'Kill 1 knight', 'Kill 1 rook']:
        if mission == 'Kill 1 bishop' and bishop == 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
        elif mission == 'Kill 1 knight' and knight == 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
        elif mission == 'Kill 1 rook' and  rook == 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    elif mission == 'Get 1 pawn killed within the first 6 moves':
        if victims.get(player_id).count('pawn') == 1 and MOVES.get(player_id)[0] <= 6:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    #MEDIUM MISSIONS
    elif mission == 'Get 1 pawn killed within the first 4 moves':
        if victims.get(player_id).count('pawn') == 1 and MOVES.get(player_id)[0] <= 4:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    elif mission == 'Kill 1 bishop and 1 knight in a single game':
        if bishop >= 1 and knight >= 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    elif mission == 'Kill 1 bishop and 1 rook in a single game':
        if bishop >= 1 and rook >= 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    elif mission == 'Kill 1 bishop, 1 rook and 1 knight in a single game':
        if bishop >= 1 and rook >= 1 and knight >= 1:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)


"""CHECK COUNT PAWN MISSIONS EITHER 2 OR 4 PAWNS"""
def check_pawns(player_id, mission, mission_id, alert_function):
    pawns_killed = victims.get(player_id).count("pawn")
    if mission == 'Eliminate all opponent pawns in a single game' and pawns_killed == 8:
        send_mission_completed(mission, player_id, mission_id, alert_function)
        update_points(mission_id, player_id)
    if mission == 'Kill 2 pawns in a single game' and pawns_killed == 2:
        send_mission_completed(mission, player_id, mission_id, alert_function)
        update_points(mission_id, player_id)
    elif mission == 'Kill 4 pawns in a single match' and pawns_killed == 4:
        send_mission_completed(mission, player_id, mission_id, alert_function)
        update_points(mission_id, player_id)
    elif mission == 'Get 4 pawns killed in a single match':
        if player_id == 0:
            pawns_killed = victims.get(1).count('pawn')
            if pawns_killed == 4:
                send_mission_completed(mission, player_id, mission_id, alert_function)
                update_points(mission_id, player_id)
        else:
            pawns_killed = victims.get(0).count('pawn')
            if pawns_killed == 4:
                send_mission_completed(mission, player_id, mission_id, alert_function)
                update_points(mission_id, player_id)

"""
CHECK KILLER-VICTIM MISSIONS BY A GIVEN PLAYER
"""
def check_kill_vic_pairs(killer, victim, player_id, mission, mission_id, alert_function):
    if (victim is not None) and kill_vic_pairs.__contains__((killer, victim)):
        KILLER = dic.get(killer)
        VICTIM = dic.get(victim)
        l = mission.split(' ')
        try:
            l.pop(l.index(KILLER))
            l.pop(l.index(VICTIM))
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
            return
        except ValueError:
            return


"""CHECK CHECK SURVIVALs"""
def check_check_counter(player_id, mission, mission_id, alert_function):
    if mission == 'Survive 3 checks in a single game':
        if CHECKS.get(player_id)[0] == 3:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)
    elif mission == 'Survive 5 checks in a single game':
        if CHECKS.get(player_id)[0] == 5:
            send_mission_completed(mission, player_id, mission_id, alert_function)
            update_points(mission_id, player_id)


def get_total_points_missions(player):
    return POINTS.get(player)[0]

def get_total_points_board(player):
    pawn = victims.get(player).count('pawn')
    bishop = victims.get(player).count('bishop')
    queen = victims.get(player).count('queen')
    rook = victims.get(player).count('rook')
    knight = victims.get(player).count('knight')



def count_moves(m, board):
    if m == 4 and board.is_checkmate():
        print("something")
    elif m <= 20 and board.is_checkmate():
        print("something")
    elif m <= 40 and board.is_checkmate():
        print("something")

