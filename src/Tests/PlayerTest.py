import unittest, sys

import chess

sys.path.append("../Chess")
import Players as Player
import ComputerPlayer as AI


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.human = Player.Player()
        self.naive = AI.Naive()
        self.smart = AI.Smart()

    def tearDown(self):
        return


    def test_get_name(self):
        self.assertEqual(self.human.get_name(), 'opponent')
        self.assertEqual(self.naive.get_name(), 'Naive')
        self.assertEqual(self.smart.get_name(), 'Smart')

    def test_set_name(self):
        self.human.set_name('Juan')
        self.naive.set_name('NAIVE')
        self.smart.set_name('SMART')
        self.assertEqual(self.human.get_name(), 'Juan')
        self.assertEqual(self.naive.get_name(), 'NAIVE')
        self.assertEqual(self.smart.get_name(), 'SMART')

    def test_make_move_naive(self):
        board = chess.Board()
        for attempt in range(10):
            move = self.naive.makeMove(board)
            self.assertTrue(board.is_legal(move))

    def test_make_move_smart(self):
        board = chess.Board()
        for attempt in range(10):
            move = self.smart.makeMove(board)
            self.assertTrue(board.is_legal(move))

if __name__ == '__main__':
    unittest.main()
