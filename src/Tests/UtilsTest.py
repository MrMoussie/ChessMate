import unittest
import src.Chess.utils as Utils
import chess


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.board = chess.Board()
        self.valid_move = 'g1f3'
        self.invalid_move = 'a8'
        self.no_move = 'hello'
        self.out_of_bounds_move = 'a1c9'
        self.some_large_string = 'I am a big string'
        self.valid_mpve_with_space = 'a1 A3'
        self.words_move = 'Echo 1 Echo 2'
        self.words = 'Echo one Echo three'

    def test_is_valid(self):
        self.assertTrue(Utils.isValid(self.valid_move))
        self.assertFalse(Utils.isValid(self.invalid_move))
        self.assertFalse(Utils.isValid(self.no_move))
        self.assertFalse(Utils.isValid(self.out_of_bounds_move))

    def test_get_normal_command(self):
        self.assertEqual(Utils.getNormalCommand(self.valid_move),'gddd 1 fddd 3')
        self.assertEqual(Utils.getNormalCommand(self.invalid_move), None)
        self.assertEqual(Utils.getNormalCommand(self.no_move), None)
        self.assertEqual(Utils.getNormalCommand(self.out_of_bounds_move), '')
        self.assertEqual(Utils.getNormalCommand(self.some_large_string), None)
        self.assertEqual(Utils.getNormalCommand(self.valid_mpve_with_space), 'addd 1 addd 3')

    def test_translate_move(self):
        self.assertEqual(Utils.traslateMove(self.words_move), 'e1e2')
        self.assertEqual(Utils.traslateMove(self.words), 'e1e3')







if __name__ == '__main__':
    unittest.main()
