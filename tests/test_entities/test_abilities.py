import pytest

from entities.abilities import Ability, Strength


class TestAbilitySkills:

    @pytest.mark.parametrize(
        "points, modifier",
        [
            (8, -1),
            (9, -1),
            (10, 0),
            (11, 0),
            (12, 1),
            (13, 1),
        ],
    )
    def test_count_modifier(self, points, modifier):
        ability = Ability(points)
        assert ability.modifier == modifier

    def test_change_points_strength(self):
        strength = Strength(12)
        assert strength.skills.athletics.modifier == 1
        assert strength.skills.saving_throw.modifier == 1

        strength.increment_points(1)
        assert strength._points == 13
        assert strength.skills.athletics.modifier == 1
        assert strength.skills.saving_throw.modifier == 1

        strength.increment_points(1)
        assert strength._points == 14
        assert strength.skills.athletics.modifier == 2
        assert strength.skills.saving_throw.modifier == 2

        strength.increment_points(-4)
        assert strength._points == 10
        assert strength.skills.athletics.modifier == 0
        assert strength.skills.saving_throw.modifier == 0
