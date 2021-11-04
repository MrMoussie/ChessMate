import unittest

import chess
sys.path.append("../Chess")
import Players as Player
import ComputerPlayer as Computer
import Rewards

class MissionsTest(unittest.TestCase):

    def setUp(self):
        self.board = chess.Board()
        self.player = Computer()
        self.mission = Rewards()

    def test_analize_move(self):
        self.assertEqual(Rewards.)


if __name__ == '__main__':
    unittest.main()
