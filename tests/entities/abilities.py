import unittest

from parameterized import parameterized

from entities.abilities import Ability


class TestAbilitySkills(unittest.TestCase):

    @parameterized.expand([
        (8, -1),
        (9, -1),
        (10, 0),
        (11, 0),
        (12, 1),
        (13, 1),
    ])
    def test_count_modifier(self, points, modifier):
        ability = Ability(points)
        self.assertEqual(ability.modifier, modifier)
