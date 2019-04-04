#!/usr/bin/env python
#
#
import unittest

class BowlingScoreTests(unittest.TestCase):

    def test_can_parse_all_strike_score_sheet(self):
        roll_count = len(Game('X X X X X X X X X X X X').rolls)
        self.assertEqual(roll_count, 12)

class Game:

    def __init__(self, scoresheet):
        self.rolls = scoresheet.split(' ')
