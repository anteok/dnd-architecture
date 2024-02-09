import pytest

from entities.abilities import AbilityPoints
from entities.character import Character
from mechanics.character.builder import HumanBuilder, ElfBuilder, HighElfBuilder, WoodElfBuilder, DrawBuilder


class TestBuilders:

    @pytest.fixture
    def character(self):
        yield Character(AbilityPoints(
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=8,
        ))

    def test_human_builder(self, character):
        human = HumanBuilder().apply_race(character)

        assert human.strength._points == 16
        assert human.athletics == 3
        assert human.strength.saving_throw == 3

        assert human.dexterity._points == 15
        assert human.stealth == 2
        assert human.sleight_of_hand == 2
        assert human.acrobatics == 2
        assert human.dexterity.saving_throw == 2

        assert human.constitution._points == 14
        assert human.constitution.saving_throw == 2

        assert human.intelligence._points == 13
        assert human.arcana == 1
        assert human.nature == 1
        assert human.history == 1
        assert human.religion == 1
        assert human.investigation == 1
        assert human.intelligence.saving_throw == 1

        assert human.wisdom._points == 11
        assert human.animal_handling == 0
        assert human.medicine == 0
        assert human.perception == 0
        assert human.insight == 0
        assert human.survival == 0
        assert human.wisdom.saving_throw == 0

        assert human.charisma._points == 9
        assert human.deception == -1
        assert human.persuasion == -1
        assert human.performance == -1
        assert human.intimidation == -1
        assert human.charisma.saving_throw == -1

        assert human.speed == 30

    def test_elf_builder(self, character):
        elf = ElfBuilder().apply_race(character)

        assert elf.strength._points == 15
        assert elf.athletics == 2
        assert elf.strength.saving_throw == 2

        assert elf.dexterity._points == 16
        assert elf.stealth == 3
        assert elf.sleight_of_hand == 3
        assert elf.acrobatics == 3
        assert elf.dexterity.saving_throw == 3

        assert elf.constitution._points == 13
        assert elf.constitution.saving_throw == 1

        assert elf.intelligence._points == 12
        assert elf.arcana == 1
        assert elf.nature == 1
        assert elf.history == 1
        assert elf.religion == 1
        assert elf.investigation == 1
        assert elf.intelligence.saving_throw == 1

        assert elf.wisdom._points == 10
        assert elf.animal_handling == 0
        assert elf.medicine == 0
        assert elf.perception == 2
        assert elf.insight == 0
        assert elf.survival == 0
        assert elf.wisdom.saving_throw == 0

        assert elf.charisma._points == 8
        assert elf.deception == -1
        assert elf.persuasion == -1
        assert elf.performance == -1
        assert elf.intimidation == -1
        assert elf.charisma.saving_throw == -1

        assert elf.speed == 30

    def test_high_elf_builder(self, character):
        elf = HighElfBuilder().apply_race(character)

        assert elf.strength._points == 15
        assert elf.athletics == 2
        assert elf.strength.saving_throw == 2

        assert elf.dexterity._points == 14
        assert elf.stealth == 2
        assert elf.sleight_of_hand == 2
        assert elf.acrobatics == 2
        assert elf.dexterity.saving_throw == 2

        assert elf.constitution._points == 13
        assert elf.constitution.saving_throw == 1

        assert elf.intelligence._points == 13
        assert elf.arcana == 1
        assert elf.nature == 1
        assert elf.history == 1
        assert elf.religion == 1
        assert elf.investigation == 1
        assert elf.intelligence.saving_throw == 1

        assert elf.wisdom._points == 10
        assert elf.animal_handling == 0
        assert elf.medicine == 0
        assert elf.perception == 2
        assert elf.insight == 0
        assert elf.survival == 0
        assert elf.wisdom.saving_throw == 0

        assert elf.charisma._points == 8
        assert elf.deception == -1
        assert elf.persuasion == -1
        assert elf.performance == -1
        assert elf.intimidation == -1
        assert elf.charisma.saving_throw == -1

        assert elf.speed == 30

    def test_wood_elf_builder(self, character):
        elf = WoodElfBuilder().apply_race(character)

        assert elf.strength._points == 15
        assert elf.athletics == 2
        assert elf.strength.saving_throw == 2

        assert elf.dexterity._points == 14
        assert elf.stealth == 2
        assert elf.sleight_of_hand == 2
        assert elf.acrobatics == 2
        assert elf.dexterity.saving_throw == 2

        assert elf.constitution._points == 13
        assert elf.constitution.saving_throw == 1

        assert elf.intelligence._points == 12
        assert elf.arcana == 1
        assert elf.nature == 1
        assert elf.history == 1
        assert elf.religion == 1
        assert elf.investigation == 1
        assert elf.intelligence.saving_throw == 1

        assert elf.wisdom._points == 11
        assert elf.animal_handling == 0
        assert elf.medicine == 0
        assert elf.perception == 2
        assert elf.insight == 0
        assert elf.survival == 0
        assert elf.wisdom.saving_throw == 0

        assert elf.charisma._points == 8
        assert elf.deception == -1
        assert elf.persuasion == -1
        assert elf.performance == -1
        assert elf.intimidation == -1
        assert elf.charisma.saving_throw == -1

        assert elf.speed == 35

    def test_draw_builder(self, character):
        elf = DrawBuilder().apply_race(character)

        assert elf.strength._points == 15
        assert elf.athletics == 2
        assert elf.strength.saving_throw == 2

        assert elf.dexterity._points == 14
        assert elf.stealth == 2
        assert elf.sleight_of_hand == 2
        assert elf.acrobatics == 2
        assert elf.dexterity.saving_throw == 2

        assert elf.constitution._points == 13
        assert elf.constitution.saving_throw == 1

        assert elf.intelligence._points == 12
        assert elf.arcana == 1
        assert elf.nature == 1
        assert elf.history == 1
        assert elf.religion == 1
        assert elf.investigation == 1
        assert elf.intelligence.saving_throw == 1

        assert elf.wisdom._points == 10
        assert elf.animal_handling == 0
        assert elf.medicine == 0
        assert elf.perception == 2
        assert elf.insight == 0
        assert elf.survival == 0
        assert elf.wisdom.saving_throw == 0

        assert elf.charisma._points == 9
        assert elf.deception == -1
        assert elf.persuasion == -1
        assert elf.performance == -1
        assert elf.intimidation == -1
        assert elf.charisma.saving_throw == -1

        assert elf.speed == 30
