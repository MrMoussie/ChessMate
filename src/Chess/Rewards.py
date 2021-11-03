import chess
import Missions

dic = {'p': 'PAWN', 'n': 'KNIGHT',
       'k': 'KING', 'q': 'QUEEN',
       'b': 'BISHOP', 'r': 'ROOK'}
victims = {0: [], 1: []}
checks = {}
pawns_killed = 0
killvic_pairs = [('p', 'p'), ('b', 'p'), ('r', 'p'), ('q', 'p'), ('n', 'p'), ('k', 'p'), ('p', 'p'), ('q', 'n'), ('q', 'q'), ('n', 'n'), ('n', 'q'), ('r', 'r'), ('b', 'b')]


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
        if killvic_pairs.__contains__((str(killer).lower(), str(victim).lower())):
            check_kill_vic_pairs(str(killer), str(victim))
    print(victims)
    return victim

def check_victims(player):
#print(no_of_victims)
    pawns_killed = (victims.get(player)).count("PAWN")
    print(pawns_killed)

def check_kill_vic_pairs(killer, victim):
        KILLER = dic.get(str(killer).lower())
        VICTIM = dic.get(str(victim).lower())
        easy = Missions.get_easy_mission()
        #medium = Missions.get_medium_mission()
        #hard = Missions.get_hard_mission()
        #expert = Missions.get_expert_mission()
        if KILLER.lower() in easy and VICTIM.lower() in easy:
            print("Mission accomplished - %s" % easy)
            #return easy                                                   Note - add the samne in the every step of if-else ladder and uncomment when database is conencted
        #elif KILLER.lower() in medium and VICTIM.lower() in medium:             Uncomment once databas is connected
        #    print("Mission accomplished - %s" % medium)
        #elif KILLER.lower() in hard and VICTIM.lower() in hard:
         #   print("Mission accomplished - %s" % hard)
        #elif KILLER.lower() in expert and VICTIM.lower() in expert:
         #   print("Mission accomplished - %s" % expert)




#   for i in range(0,no_of_victims):
#     if ((victims.get(player))[i] == "PAWN") :
