"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer(1)
        self.player2 = game_agent.AlphaBetaPlayer()
        self.game = isolation.Board(self.player1, self.player2, 5, 5)

    def test_minimax(self):

        time_limit = 150000
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda: time_limit - (time_millis() - move_start)
        # self.game.apply_move((2,2))
        # self.game.apply_move((0, 2))
        self.game.to_string()
        self.player1.time_left = time_left
        self.assertEqual(self.player1.minimax(self.game, 7), (2, 2))

    def test_alphabeta(self):

        time_limit = 150000
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda: time_limit - (time_millis() - move_start)
        # self.game.apply_move((2,2))
        # self.game.apply_move((0, 2))
        self.game.to_string()
        self.player2.time_left = time_left
        self.assertEqual(self.player2.alphabeta(self.game, 7), (2, 2))


if __name__ == '__main__':
    unittest.main()
