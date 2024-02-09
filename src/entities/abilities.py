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

    @property
    def saving_throw(self):
        return self.skills.saving_throw.value

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


class Charisma(Ability[CharismaSkills]):
    _ability_skills_class = CharismaSkills


@dataclass
class AbilityPoints:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class StrengthMixin:

    def __init__(self, ability_points: AbilityPoints):
        self.strength = Strength(ability_points.strength)

    @property
    def athletics(self):
        return self.strength.skills.athletics.value


class DexterityMixin:
    def __init__(self, ability_points: AbilityPoints):
        self.dexterity = Dexterity(ability_points.dexterity)

    @property
    def acrobatics(self):
        return self.dexterity.skills.acrobatics.value

    @property
    def sleight_of_hand(self):
        return self.dexterity.skills.sleight_of_hand.value

    @property
    def stealth(self):
        return self.dexterity.skills.stealth.value


class ConstitutionMixin:
    def __init__(self, ability_points: AbilityPoints):
        self.constitution = Constitution(ability_points.constitution)


class IntelligenceMixin:
    def __init__(self, ability_points: AbilityPoints):
        self.intelligence = Intelligence(ability_points.intelligence)

    @property
    def arcana(self):
        return self.intelligence.skills.arcana.value

    @property
    def nature(self):
        return self.intelligence.skills.nature.value

    @property
    def history(self):
        return self.intelligence.skills.history.value

    @property
    def investigation(self):
        return self.intelligence.skills.investigation.value

    @property
    def religion(self):
        return self.intelligence.skills.religion.value


class WisdomMixin:
    def __init__(self, ability_points: AbilityPoints):
        self.wisdom = Wisdom(ability_points.wisdom)

    @property
    def animal_handling(self):
        return self.wisdom.skills.animal_handling.value

    @property
    def medicine(self):
        return self.wisdom.skills.medicine.value

    @property
    def perception(self):
        return self.wisdom.skills.perception.value

    @property
    def insight(self):
        return self.wisdom.skills.insight.value

    @property
    def survival(self):
        return self.wisdom.skills.survival.value


class CharismaMixin:
    def __init__(self, ability_points: AbilityPoints):
        self.charisma = Charisma(ability_points.charisma)

    @property
    def deception(self):
        return self.charisma.skills.deception.value

    @property
    def intimidation(self):
        return self.charisma.skills.intimidation.value

    @property
    def performance(self):
        return self.charisma.skills.performance.value

    @property
    def persuasion(self):
        return self.charisma.skills.persuasion.value
