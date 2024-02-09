import pytest

from entities.abilities import AbilityPoints
from entities.character import Character
from mechanics.character.builder import HumanBuilder, ElfBuilder, HighElfBuilder, WoodElfBuilder, DrawBuilder, \
    GnomeBuilder, ForestGnomeBuilder, RockGnomeBuilder, HillDwarfBuilder, MountainDwarfBuilder, DragonbornBuilder, \
    HalfOrcBuilder, HalflingBuilder, StoutHalflingBuilder, LightfootHalflingBuilder


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

        assert elf.dexterity._points == 16
        assert elf.stealth == 3
        assert elf.sleight_of_hand == 3
        assert elf.acrobatics == 3
        assert elf.dexterity.saving_throw == 3

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

        assert elf.charisma._points == 9
        assert elf.deception == -1
        assert elf.persuasion == -1
        assert elf.performance == -1
        assert elf.intimidation == -1
        assert elf.charisma.saving_throw == -1

        assert elf.speed == 30

    def test_gnome_builder(self, character):
        gnome = GnomeBuilder().apply_race(character)

        assert gnome.strength._points == 15
        assert gnome.athletics == 2
        assert gnome.strength.saving_throw == 2

        assert gnome.dexterity._points == 14
        assert gnome.stealth == 2
        assert gnome.sleight_of_hand == 2
        assert gnome.acrobatics == 2
        assert gnome.dexterity.saving_throw == 2

        assert gnome.constitution._points == 13
        assert gnome.constitution.saving_throw == 1

        assert gnome.intelligence._points == 14
        assert gnome.arcana == 2
        assert gnome.nature == 2
        assert gnome.history == 2
        assert gnome.religion == 2
        assert gnome.investigation == 2
        assert gnome.intelligence.saving_throw == 2

        assert gnome.wisdom._points == 10
        assert gnome.animal_handling == 0
        assert gnome.medicine == 0
        assert gnome.perception == 0
        assert gnome.insight == 0
        assert gnome.survival == 0
        assert gnome.wisdom.saving_throw == 0

        assert gnome.charisma._points == 8
        assert gnome.deception == -1
        assert gnome.persuasion == -1
        assert gnome.performance == -1
        assert gnome.intimidation == -1
        assert gnome.charisma.saving_throw == -1

        assert gnome.speed == 25

    def test_forest_gnome_builder(self, character):
        gnome = ForestGnomeBuilder().apply_race(character)

        assert gnome.strength._points == 15
        assert gnome.athletics == 2
        assert gnome.strength.saving_throw == 2

        assert gnome.dexterity._points == 15
        assert gnome.stealth == 2
        assert gnome.sleight_of_hand == 2
        assert gnome.acrobatics == 2
        assert gnome.dexterity.saving_throw == 2

        assert gnome.constitution._points == 13
        assert gnome.constitution.saving_throw == 1

        assert gnome.intelligence._points == 14
        assert gnome.arcana == 2
        assert gnome.nature == 2
        assert gnome.history == 2
        assert gnome.religion == 2
        assert gnome.investigation == 2
        assert gnome.intelligence.saving_throw == 2

        assert gnome.wisdom._points == 10
        assert gnome.animal_handling == 0
        assert gnome.medicine == 0
        assert gnome.perception == 0
        assert gnome.insight == 0
        assert gnome.survival == 0
        assert gnome.wisdom.saving_throw == 0

        assert gnome.charisma._points == 8
        assert gnome.deception == -1
        assert gnome.persuasion == -1
        assert gnome.performance == -1
        assert gnome.intimidation == -1
        assert gnome.charisma.saving_throw == -1

        assert gnome.speed == 25

    def test_rock_gnome_builder(self, character):
        gnome = RockGnomeBuilder().apply_race(character)

        assert gnome.strength._points == 15
        assert gnome.athletics == 2
        assert gnome.strength.saving_throw == 2

        assert gnome.dexterity._points == 14
        assert gnome.stealth == 2
        assert gnome.sleight_of_hand == 2
        assert gnome.acrobatics == 2
        assert gnome.dexterity.saving_throw == 2

        assert gnome.constitution._points == 14
        assert gnome.constitution.saving_throw == 2

        assert gnome.intelligence._points == 14
        assert gnome.arcana == 2
        assert gnome.nature == 2
        assert gnome.history == 2
        assert gnome.religion == 2
        assert gnome.investigation == 2
        assert gnome.intelligence.saving_throw == 2

        assert gnome.wisdom._points == 10
        assert gnome.animal_handling == 0
        assert gnome.medicine == 0
        assert gnome.perception == 0
        assert gnome.insight == 0
        assert gnome.survival == 0
        assert gnome.wisdom.saving_throw == 0

        assert gnome.charisma._points == 8
        assert gnome.deception == -1
        assert gnome.persuasion == -1
        assert gnome.performance == -1
        assert gnome.intimidation == -1
        assert gnome.charisma.saving_throw == -1

        assert gnome.speed == 25

    def test_hill_dwarf_builder(self, character):
        dwarf = HillDwarfBuilder().apply_race(character)

        assert dwarf.strength._points == 15
        assert dwarf.athletics == 2
        assert dwarf.strength.saving_throw == 2

        assert dwarf.dexterity._points == 14
        assert dwarf.stealth == 2
        assert dwarf.sleight_of_hand == 2
        assert dwarf.acrobatics == 2
        assert dwarf.dexterity.saving_throw == 2

        assert dwarf.constitution._points == 15
        assert dwarf.constitution.saving_throw == 2

        assert dwarf.intelligence._points == 12
        assert dwarf.arcana == 1
        assert dwarf.nature == 1
        assert dwarf.history == 1
        assert dwarf.religion == 1
        assert dwarf.investigation == 1
        assert dwarf.intelligence.saving_throw == 1

        assert dwarf.wisdom._points == 11
        assert dwarf.animal_handling == 0
        assert dwarf.medicine == 0
        assert dwarf.perception == 0
        assert dwarf.insight == 0
        assert dwarf.survival == 0
        assert dwarf.wisdom.saving_throw == 0

        assert dwarf.charisma._points == 8
        assert dwarf.deception == -1
        assert dwarf.persuasion == -1
        assert dwarf.performance == -1
        assert dwarf.intimidation == -1
        assert dwarf.charisma.saving_throw == -1

        assert dwarf.speed == 25

    def test_mountain_dwarf_builder(self, character):
        dwarf = MountainDwarfBuilder().apply_race(character)

        assert dwarf.strength._points == 17
        assert dwarf.athletics == 3
        assert dwarf.strength.saving_throw == 3

        assert dwarf.dexterity._points == 14
        assert dwarf.stealth == 2
        assert dwarf.sleight_of_hand == 2
        assert dwarf.acrobatics == 2
        assert dwarf.dexterity.saving_throw == 2

        assert dwarf.constitution._points == 15
        assert dwarf.constitution.saving_throw == 2

        assert dwarf.intelligence._points == 12
        assert dwarf.arcana == 1
        assert dwarf.nature == 1
        assert dwarf.history == 1
        assert dwarf.religion == 1
        assert dwarf.investigation == 1
        assert dwarf.intelligence.saving_throw == 1

        assert dwarf.wisdom._points == 10
        assert dwarf.animal_handling == 0
        assert dwarf.medicine == 0
        assert dwarf.perception == 0
        assert dwarf.insight == 0
        assert dwarf.survival == 0
        assert dwarf.wisdom.saving_throw == 0

        assert dwarf.charisma._points == 8
        assert dwarf.deception == -1
        assert dwarf.persuasion == -1
        assert dwarf.performance == -1
        assert dwarf.intimidation == -1
        assert dwarf.charisma.saving_throw == -1

        assert dwarf.speed == 25

    def test_dragonborn_builder(self, character):
        dragonborn = DragonbornBuilder().apply_race(character)

        assert dragonborn.strength._points == 17
        assert dragonborn.athletics == 3
        assert dragonborn.strength.saving_throw == 3

        assert dragonborn.dexterity._points == 14
        assert dragonborn.stealth == 2
        assert dragonborn.sleight_of_hand == 2
        assert dragonborn.acrobatics == 2
        assert dragonborn.dexterity.saving_throw == 2

        assert dragonborn.constitution._points == 13
        assert dragonborn.constitution.saving_throw == 1

        assert dragonborn.intelligence._points == 12
        assert dragonborn.arcana == 1
        assert dragonborn.nature == 1
        assert dragonborn.history == 1
        assert dragonborn.religion == 1
        assert dragonborn.investigation == 1
        assert dragonborn.intelligence.saving_throw == 1

        assert dragonborn.wisdom._points == 10
        assert dragonborn.animal_handling == 0
        assert dragonborn.medicine == 0
        assert dragonborn.perception == 0
        assert dragonborn.insight == 0
        assert dragonborn.survival == 0
        assert dragonborn.wisdom.saving_throw == 0

        assert dragonborn.charisma._points == 9
        assert dragonborn.deception == -1
        assert dragonborn.persuasion == -1
        assert dragonborn.performance == -1
        assert dragonborn.intimidation == -1
        assert dragonborn.charisma.saving_throw == -1

        assert dragonborn.speed == 30

    def test_half_orc_builder(self, character):
        dragonborn = HalfOrcBuilder().apply_race(character)

        assert dragonborn.strength._points == 17
        assert dragonborn.athletics == 3
        assert dragonborn.strength.saving_throw == 3

        assert dragonborn.dexterity._points == 14
        assert dragonborn.stealth == 2
        assert dragonborn.sleight_of_hand == 2
        assert dragonborn.acrobatics == 2
        assert dragonborn.dexterity.saving_throw == 2

        assert dragonborn.constitution._points == 14
        assert dragonborn.constitution.saving_throw == 2

        assert dragonborn.intelligence._points == 12
        assert dragonborn.arcana == 1
        assert dragonborn.nature == 1
        assert dragonborn.history == 1
        assert dragonborn.religion == 1
        assert dragonborn.investigation == 1
        assert dragonborn.intelligence.saving_throw == 1

        assert dragonborn.wisdom._points == 10
        assert dragonborn.animal_handling == 0
        assert dragonborn.medicine == 0
        assert dragonborn.perception == 0
        assert dragonborn.insight == 0
        assert dragonborn.survival == 0
        assert dragonborn.wisdom.saving_throw == 0

        assert dragonborn.charisma._points == 8
        assert dragonborn.deception == -1
        assert dragonborn.persuasion == -1
        assert dragonborn.performance == -1
        assert dragonborn.intimidation == 1
        assert dragonborn.charisma.saving_throw == -1

        assert dragonborn.speed == 30

    def test_halfling_builder(self, character):
        halfling = HalflingBuilder().apply_race(character)

        assert halfling.strength._points == 15
        assert halfling.athletics == 2
        assert halfling.strength.saving_throw == 2

        assert halfling.dexterity._points == 16
        assert halfling.stealth == 3
        assert halfling.sleight_of_hand == 3
        assert halfling.acrobatics == 3
        assert halfling.dexterity.saving_throw == 3

        assert halfling.constitution._points == 13
        assert halfling.constitution.saving_throw == 1

        assert halfling.intelligence._points == 12
        assert halfling.arcana == 1
        assert halfling.nature == 1
        assert halfling.history == 1
        assert halfling.religion == 1
        assert halfling.investigation == 1
        assert halfling.intelligence.saving_throw == 1

        assert halfling.wisdom._points == 10
        assert halfling.animal_handling == 0
        assert halfling.medicine == 0
        assert halfling.perception == 0
        assert halfling.insight == 0
        assert halfling.survival == 0
        assert halfling.wisdom.saving_throw == 0

        assert halfling.charisma._points == 8
        assert halfling.deception == -1
        assert halfling.persuasion == -1
        assert halfling.performance == -1
        assert halfling.intimidation == -1
        assert halfling.charisma.saving_throw == -1

        assert halfling.speed == 25

    def test_stout_halfling_builder(self, character):
        halfling = StoutHalflingBuilder().apply_race(character)

        assert halfling.strength._points == 15
        assert halfling.athletics == 2
        assert halfling.strength.saving_throw == 2

        assert halfling.dexterity._points == 16
        assert halfling.stealth == 3
        assert halfling.sleight_of_hand == 3
        assert halfling.acrobatics == 3
        assert halfling.dexterity.saving_throw == 3

        assert halfling.constitution._points == 14
        assert halfling.constitution.saving_throw == 2

        assert halfling.intelligence._points == 12
        assert halfling.arcana == 1
        assert halfling.nature == 1
        assert halfling.history == 1
        assert halfling.religion == 1
        assert halfling.investigation == 1
        assert halfling.intelligence.saving_throw == 1

        assert halfling.wisdom._points == 10
        assert halfling.animal_handling == 0
        assert halfling.medicine == 0
        assert halfling.perception == 0
        assert halfling.insight == 0
        assert halfling.survival == 0
        assert halfling.wisdom.saving_throw == 0

        assert halfling.charisma._points == 8
        assert halfling.deception == -1
        assert halfling.persuasion == -1
        assert halfling.performance == -1
        assert halfling.intimidation == -1
        assert halfling.charisma.saving_throw == -1

        assert halfling.speed == 25

    def test_lightfoot_halfling_builder(self, character):
        halfling = LightfootHalflingBuilder().apply_race(character)

        assert halfling.strength._points == 15
        assert halfling.athletics == 2
        assert halfling.strength.saving_throw == 2

        assert halfling.dexterity._points == 16
        assert halfling.stealth == 3
        assert halfling.sleight_of_hand == 3
        assert halfling.acrobatics == 3
        assert halfling.dexterity.saving_throw == 3

        assert halfling.constitution._points == 13
        assert halfling.constitution.saving_throw == 1

        assert halfling.intelligence._points == 12
        assert halfling.arcana == 1
        assert halfling.nature == 1
        assert halfling.history == 1
        assert halfling.religion == 1
        assert halfling.investigation == 1
        assert halfling.intelligence.saving_throw == 1

        assert halfling.wisdom._points == 10
        assert halfling.animal_handling == 0
        assert halfling.medicine == 0
        assert halfling.perception == 0
        assert halfling.insight == 0
        assert halfling.survival == 0
        assert halfling.wisdom.saving_throw == 0

        assert halfling.charisma._points == 9
        assert halfling.deception == -1
        assert halfling.persuasion == -1
        assert halfling.performance == -1
        assert halfling.intimidation == -1
        assert halfling.charisma.saving_throw == -1

        assert halfling.speed == 25
