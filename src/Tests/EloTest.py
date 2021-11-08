import unittest
import sys
sys.path.append('../Chess')
from elo import *
from Players import Player

player1 = Player()
player2 = Player()
player1.set_name('player 1')
player2.set_name('player 2')

class MyTestCase(unittest.TestCase):
    def test_process_elo_p1win(self):
        player1.set_elo(1000)
        player2.set_elo(500)
        p1score = 1004
        p2score = 496
        process_elo(player1, player2, False)
        self.assertEquals(round(player1.get_elo()), p1score)
        self.assertEquals(round(player2.get_elo()), p2score)

    def test_process_elo_p2win(self):
        player1.set_elo(1000)
        player2.set_elo(500)
        p1score = 920
        p2score = 580
        process_elo(player2, player1, False)
        self.assertEquals(round(player1.get_elo()), p1score)
        self.assertEquals(round(player2.get_elo()), p2score)

    def test_process_elo_draw(self):
        player1.set_elo(1000)
        player2.set_elo(500)
        p1score = 962
        p2score = 538
        process_elo(player1, player2, True)
        self.assertEquals(round(player1.get_elo()), p1score)
        self.assertEquals(round(player2.get_elo()), p2score)


if __name__ == '__main__':
    unittest.main()
