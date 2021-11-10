from EloPy.elopy import *
from Players import Player

import sys
sys.path.append('../Chess')

def process_elo(winner, loser, draw):
    i = Implementation()
    player1 = winner.get_name()
    player2 = loser.get_name()
    elo1 = winner.get_elo()
    elo2 = loser.get_elo()
    i.addPlayer(player1, elo1)
    i.addPlayer(player2, elo2)
    if draw:
        i.recordMatch(player1, player2, draw=draw)
    else:
        i.recordMatch(player1, player2, winner=player1)
    winner.set_elo(i.getRatingList()[0][1])
    loser.set_elo(i.getRatingList()[1][1])