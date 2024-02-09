from abc import abstractmethod
from typing import Optional

from entities.abilities import (
    AbilityPoints,
    Strength,
    Dexterity,
    Constitution,
    Intelligence,
    Wisdom,
    Charisma,
    Ability, StrengthMixin, DexterityMixin, IntelligenceMixin, WisdomMixin, CharismaMixin, ConstitutionMixin,
)


class Character(
    StrengthMixin,
    DexterityMixin,
    IntelligenceMixin,
    ConstitutionMixin,
    WisdomMixin,
    CharismaMixin,
):
    level = 1
    proficiency = 2
    spelling_ability: Optional[Ability] = None
    health_points = 0
    max_health_points = 0
    armor_value = 0
    speed = 0

    def __init__(self, ability_points: AbilityPoints):
        StrengthMixin.__init__(self, ability_points)
        DexterityMixin.__init__(self, ability_points)
        IntelligenceMixin.__init__(self, ability_points)
        ConstitutionMixin.__init__(self, ability_points)
        WisdomMixin.__init__(self, ability_points)
        CharismaMixin.__init__(self, ability_points)

