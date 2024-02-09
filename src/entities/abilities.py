from dataclasses import dataclass
from typing import Type, Optional, TypeVar, Generic

from entities.skills import (
    AbilitySkills,
    StrengthSkills,
    DexteritySkills,
    IntelligenceSkills,
    WisdomSkills,
    CharismaSkills,
    ConstitutionSkills,
)


T = TypeVar("T", bound=AbilitySkills)


class Ability(Generic[T]):
    _ability_skills_class: Optional[Type[T]] = None

    def __init__(self, points_used: int) -> None:
        self._points = points_used
        self.modifier = self._count_modifier(points_used)
        self.skills: T = (
            self._ability_skills_class(self.modifier)
            if self._ability_skills_class
            else None
        )

    def _count_modifier(self, points: int) -> int:
        return points // 2 - 5

    def increment_points(self, value):
        self._points += value
        new_modifier = self._count_modifier(self._points)
        if new_modifier != self.modifier:
            if self.skills:
                self.skills.increment_all_modifiers(new_modifier - self.modifier)
            self.modifier = new_modifier


class Strength(Ability[StrengthSkills]):
    _ability_skills_class = StrengthSkills


class Dexterity(Ability[DexteritySkills]):
    _ability_skills_class = DexteritySkills


class Constitution(Ability[ConstitutionSkills]):
    _ability_skills_class = ConstitutionSkills


class Intelligence(Ability[IntelligenceSkills]):
    _ability_skills_class = IntelligenceSkills


class Wisdom(Ability[WisdomSkills]):
    _ability_skills_class = WisdomSkills


class Charisma(Ability):
    _ability_skills_class = CharismaSkills


@dataclass
class AbilityPoints:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
