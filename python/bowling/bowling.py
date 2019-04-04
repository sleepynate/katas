#!/usr/bin/env python
#
#
import unittest

class BowlingScoreTests(unittest.TestCase):

    def test_can_parse_all_strike_score_sheet(self):
        """Can parse score sheet with all strikes"""
        roll_count = len(Game('X X X X X X X X X X X X').rolls)
        self.assertEqual(roll_count, 12)

    def test_can_parse_no_pickup_score_sheet(self):
        """Can parse score sheet with no pickup rolls"""
        roll_count = len(Game('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-').rolls)
        self.assertEqual(roll_count, 20)

    def test_can_parse_very_short_game(self):
        """Can parse a game with only one roll"""
        roll_count = len(Game('1').rolls)
        self.assertEqual(roll_count, 1)

    def test_can_score_very_short_game(self):
        """Can score a game with only one roll"""
        self.assertEqual(Game('1').score(), 1)

class FlattenTests(unittest.TestCase):
    def test_can_flatten_list(self):
        """Can flatten a list of lists to a 1-dimensional list"""
        self.assertEqual(flatten([[1,2], [3,4]]), [1,2,3,4])

def flatten(lst):
    return [item for sublist in lst for item in sublist]

class Game:

    def __init__(self, scoresheet):
        scoresheet_by_frame = map(lambda x: list(x), scoresheet.split(' '))
        self.rolls = flatten(scoresheet_by_frame)

    def score(self):
        return sum(map(int, self.rolls))
