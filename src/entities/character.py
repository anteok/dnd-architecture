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
    Ability,
)


class Character:
    spelling_ability: Optional[Ability] = None
    health_points = 0
    max_health_points = 0
    armor_value = 0
    speed = 0

    def __init__(self, ability_points: AbilityPoints):

        self.strength = Strength(ability_points.strength)
        self.dexterity = Dexterity(ability_points.dexterity)
        self.constitution = Constitution(ability_points.constitution)
        self.intelligence = Intelligence(ability_points.intelligence)
        self.wisdom = Wisdom(ability_points.wisdom)
        self.charisma = Charisma(ability_points.charisma)
