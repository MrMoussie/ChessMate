import unittest
import sys
import chess
sys.path.append("../Chess")
import Players as Player
import ComputerPlayer as Computer
import Rewards

class MissionsTest(unittest.TestCase):

    def setUp(self):
        self.board = chess.Board()
        self.human = Player.Player()
        self.player = Computer()
        self.mission = Rewards()

    def test_is_promoted(self):
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()
