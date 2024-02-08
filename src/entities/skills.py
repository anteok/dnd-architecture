from dataclasses import dataclass

from entities.enums.skills import (
    SkillsEnum, StrengthSkillsEnum, DexteritySkillsEnum, IntelligenceSkillsEnum,
    WisdomSkillsEnum, CharismaSkillsEnum
)


@dataclass
class SkillValue:
    modifier: int
    is_proficient: bool = False


class AbilitySkills:
    _skills_enum: SkillsEnum

    def __init__(self, modifier: int) -> None:
        self._skills_container = {skill: SkillValue(modifier) for skill in self._skills_enum}


class StrengthSkills(AbilitySkills):
    _skills_enum = StrengthSkillsEnum

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.athletics = self._skills_container[StrengthSkillsEnum.athletics]


class DexteritySkills(AbilitySkills):
    _skills_enum = DexteritySkillsEnum

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.acrobatics = self._skills_container[DexteritySkillsEnum.acrobatics]
        self.sleight_of_hand = self._skills_container[DexteritySkillsEnum.sleight_of_hand]
        self.stealth = self._skills_container[DexteritySkillsEnum.stealth]


class IntelligenceSkills(AbilitySkills):
    _skills_enum = IntelligenceSkillsEnum

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.arcana = self._skills_container[IntelligenceSkillsEnum.arcana]
        self.history = self._skills_container[IntelligenceSkillsEnum.history]
        self.investigation = self._skills_container[IntelligenceSkillsEnum.investigation]
        self.religion = self._skills_container[IntelligenceSkillsEnum.religion]
        self.nature = self._skills_container[IntelligenceSkillsEnum.nature]


class WisdomSkills(AbilitySkills):
    _skills_enum = WisdomSkillsEnum

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.animal_handling = self._skills_container[WisdomSkillsEnum.animal_handling]
        self.insight = self._skills_container[WisdomSkillsEnum.insight]
        self.medicine = self._skills_container[WisdomSkillsEnum.medicine]
        self.perception = self._skills_container[WisdomSkillsEnum.perception]
        self.survival = self._skills_container[WisdomSkillsEnum.survival]


class CharismaSkills(AbilitySkills):
    _skills_enum = CharismaSkillsEnum

    def __init__(self, modifier: int):
        super().__init__(modifier)
        self.deception = self._skills_container[CharismaSkillsEnum.deception]
        self.intimidation = self._skills_container[CharismaSkillsEnum.intimidation]
        self.persuasion = self._skills_container[CharismaSkillsEnum.persuasion]
        self.performance = self._skills_container[CharismaSkillsEnum.performance]
