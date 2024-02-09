from enum import Enum


class SkillsNames(str, Enum): ...


class StrengthSkillsNames(SkillsNames, Enum):
    athletics = "athletics"
    saving_throw = "saving_throw"


class DexteritySkillsNames(SkillsNames, Enum):
    acrobatics = "acrobatics"
    sleight_of_hand = "sleight_of_hand"
    stealth = "stealth"
    saving_throw = "saving_throw"


class IntelligenceSkillsNames(SkillsNames, Enum):
    arcana = "arcana"
    history = "history"
    investigation = "investigation"
    religion = "religion"
    nature = "nature"
    saving_throw = "saving_throw"


class ConstitutionSkillsNames(SkillsNames, Enum):
    saving_throw = "saving_throw"


class WisdomSkillsNames(SkillsNames, Enum):
    animal_handling = "animal_handling"
    insight = "insight"
    medicine = "medicine"
    perception = "perception"
    survival = "survival"
    saving_throw = "saving_throw"


class CharismaSkillsNames(SkillsNames, Enum):
    deception = "deception"
    intimidation = "intimidation"
    performance = "performance"
    persuasion = "persuasion"
    saving_throw = "saving_throw"
