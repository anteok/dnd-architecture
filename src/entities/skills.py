from dataclasses import dataclass

from entities.enums.skills import (
    SkillsNames,
    StrengthSkillsNames,
    DexteritySkillsNames,
    IntelligenceSkillsNames,
    WisdomSkillsNames,
    CharismaSkillsNames,
    ConstitutionSkillsNames,
)


@dataclass
class SkillValue:
    modifier: int
    is_proficient: bool = False


class AbilitySkills:
    _skills_names: SkillsNames

    def __init__(self, modifier: int) -> None:
        self._skills_container = {
            skill_name: SkillValue(modifier) for skill_name in self._skills_names
        }

    def increment_all_modifiers(self, value: int) -> None:
        for skill in self._skills_container.values():
            skill.modifier += value


class StrengthSkills(AbilitySkills):
    _skills_names = StrengthSkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.athletics = self._skills_container[StrengthSkillsNames.athletics]
        self.saving_throw = self._skills_container[StrengthSkillsNames.saving_throw]


class DexteritySkills(AbilitySkills):
    _skills_names = DexteritySkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.acrobatics = self._skills_container[DexteritySkillsNames.acrobatics]
        self.sleight_of_hand = self._skills_container[
            DexteritySkillsNames.sleight_of_hand
        ]
        self.stealth = self._skills_container[DexteritySkillsNames.stealth]
        self.saving_throw = self._skills_container[DexteritySkillsNames.saving_throw]


class ConstitutionSkills(AbilitySkills):
    _skills_names = ConstitutionSkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.saving_throw = self._skills_container[ConstitutionSkillsNames.saving_throw]


class IntelligenceSkills(AbilitySkills):
    _skills_names = IntelligenceSkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.arcana = self._skills_container[IntelligenceSkillsNames.arcana]
        self.history = self._skills_container[IntelligenceSkillsNames.history]
        self.investigation = self._skills_container[
            IntelligenceSkillsNames.investigation
        ]
        self.religion = self._skills_container[IntelligenceSkillsNames.religion]
        self.nature = self._skills_container[IntelligenceSkillsNames.nature]
        self.saving_throw = self._skills_container[IntelligenceSkillsNames.saving_throw]


class WisdomSkills(AbilitySkills):
    _skills_names = WisdomSkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.animal_handling = self._skills_container[WisdomSkillsNames.animal_handling]
        self.insight = self._skills_container[WisdomSkillsNames.insight]
        self.medicine = self._skills_container[WisdomSkillsNames.medicine]
        self.perception = self._skills_container[WisdomSkillsNames.perception]
        self.survival = self._skills_container[WisdomSkillsNames.survival]
        self.saving_throw = self._skills_container[WisdomSkillsNames.saving_throw]


class CharismaSkills(AbilitySkills):
    _skills_names = CharismaSkillsNames

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.deception = self._skills_container[CharismaSkillsNames.deception]
        self.intimidation = self._skills_container[CharismaSkillsNames.intimidation]
        self.persuasion = self._skills_container[CharismaSkillsNames.persuasion]
        self.performance = self._skills_container[CharismaSkillsNames.performance]
        self.saving_throw = self._skills_container[CharismaSkillsNames.saving_throw]
