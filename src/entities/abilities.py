from dataclasses import dataclass
from typing import Type, Optional

from entities.skills import AbilitySkills, StrengthSkills, DexteritySkills, IntelligenceSkills, WisdomSkills, \
    CharismaSkills


@dataclass
class AbilityPoints:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class Ability:
    _ability_skills_class: Optional[Type[AbilitySkills]] = None

    def __init__(self, points_used: int) -> None:
        self._points = points_used
        self.modifier = self._count_modifier(points_used)
        self.saving_throw = self.modifier
        self.skills = self._ability_skills_class(self.modifier) if self._ability_skills_class else None

    def _count_modifier(self, points: int) -> int:
        return points // 2 - 5


class Strength(Ability):
    _ability_skills_class = StrengthSkills


class Dexterity(Ability):
    _ability_skills_class = DexteritySkills


class Constitution(Ability):
    ...


class Intelligence(Ability):
    _ability_skills_class = IntelligenceSkills


class Wisdom(Ability):
    _ability_skills_class = WisdomSkills


class Charisma(Ability):
    _ability_skills_class = CharismaSkills
