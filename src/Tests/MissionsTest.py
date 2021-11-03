import unittest

import chess
sys.path.append("../Chess")
import Players as Player
import ComputerPlayer as Computer
import Missions

class MissionsTest(unittest.TestCase):

    def setUp(self):
        self.board = chess.Board()
        self.player = Computer()
        self.mission = Missions()

    def test_analize_move(self):
        self.assertEqual(self.mission)


if __name__ == '__main__':
    unittest.main()
