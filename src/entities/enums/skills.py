from enum import Enum


class SkillsEnum(str, Enum):
    ...


class StrengthSkillsEnum(SkillsEnum, Enum):
    athletics = 'athletics'


class DexteritySkillsEnum(SkillsEnum, Enum):
    acrobatics = 'acrobatics'
    sleight_of_hand = 'sleight_of_hand'
    stealth = 'stealth'


class IntelligenceSkillsEnum(SkillsEnum, Enum):
    arcana = 'arcana'
    history = 'history'
    investigation = 'investigation'
    religion = 'religion'
    nature = 'nature'


class WisdomSkillsEnum(SkillsEnum, Enum):
    animal_handling = 'animal_handling'
    insight = 'insight'
    medicine = 'medicine'
    perception = 'perception'
    survival = 'survival'


class CharismaSkillsEnum(SkillsEnum, Enum):
    deception = 'deception'
    intimidation = 'intimidation'
    performance = 'performance'
    persuasion = 'persuasion'
