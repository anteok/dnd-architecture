from abc import abstractmethod, ABCMeta

from entities.character import Character
from entities.enums.races import Races


class AbstractRaceBuilder(metaclass=ABCMeta):
    _race: Races

    @abstractmethod
    def apply_race(self, character: Character) -> Character:
        ...


class BaseElfBuilderMixin:

    def _apply_default(self, character: Character) -> None:
        character.dexterity.increment_points(2)
        character.wisdom.skills.perception.proficiency = character.proficiency
        character.speed = 30


class BaseGnomeBuilderMixin:

    def _apply_default(self, character: Character) -> None:
        character.intelligence.increment_points(2)
        character.speed = 25


class BaseDwarfBuilderMixin:

    def _apply_default(self, character: Character) -> None:
        character.constitution.increment_points(2)
        character.speed = 25


class BaseHalflingBuilderMixin:

    def _apply_default(self, character: Character) -> None:
        character.dexterity.increment_points(2)
        character.speed = 25


class HumanBuilder(AbstractRaceBuilder):
    _race = Races.human

    def apply_race(self, character: Character) -> Character:
        character.strength.increment_points(1)
        character.dexterity.increment_points(1)
        character.constitution.increment_points(1)
        character.intelligence.increment_points(1)
        character.wisdom.increment_points(1)
        character.charisma.increment_points(1)

        character.speed = 30
        return character


class ElfBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.elf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        return character


class HighElfBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.high_elf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.intelligence.increment_points(1)
        return character


class WoodElfBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.wood_elf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.wisdom.increment_points(1)
        character.speed = 35
        return character


class DrawBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.draw

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.charisma.increment_points(1)
        return character


class GnomeBuilder(AbstractRaceBuilder, BaseGnomeBuilderMixin):
    _race = Races.gnome

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        return character


class ForestGnomeBuilder(AbstractRaceBuilder, BaseGnomeBuilderMixin):
    _race = Races.forest_gnome

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.dexterity.increment_points(1)
        return character


class RockGnomeBuilder(AbstractRaceBuilder, BaseGnomeBuilderMixin):
    _race = Races.rock_gnome

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.constitution.increment_points(1)
        return character


class HillDwarfBuilder(AbstractRaceBuilder, BaseDwarfBuilderMixin):
    _race = Races.hill_dwarf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.wisdom.increment_points(1)
        return character


class MountainDwarfBuilder(AbstractRaceBuilder, BaseDwarfBuilderMixin):
    _race = Races.mountain_dwarf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.strength.increment_points(2)
        return character


class DragonbornBuilder(AbstractRaceBuilder):
    _race = Races.dragonborn

    def apply_race(self, character: Character) -> Character:
        character.strength.increment_points(2)
        character.charisma.increment_points(1)
        character.speed = 30
        return character


class HalfOrcBuilder(AbstractRaceBuilder):
    _race = Races.half_orc

    def apply_race(self, character: Character) -> Character:
        character.strength.increment_points(2)
        character.constitution.increment_points(1)
        character.charisma.skills.intimidation.proficiency = character.proficiency
        character.speed = 30
        return character


class HalflingBuilder(AbstractRaceBuilder, BaseHalflingBuilderMixin):
    _race = Races.halfling

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        return character


class StoutHalflingBuilder(AbstractRaceBuilder, BaseHalflingBuilderMixin):
    _race = Races.stout_halfling

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.constitution.increment_points(1)
        return character


class LightfootHalflingBuilder(AbstractRaceBuilder, BaseHalflingBuilderMixin):
    _race = Races.lightfoot_halfling

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.charisma.increment_points(1)
        return character


class HalfElfBuilder(AbstractRaceBuilder):
    _race = Races.half_elf

    def apply_race(self, character: Character) -> Character:
        # how to use randomly given points?
