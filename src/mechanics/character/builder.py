from abc import abstractmethod, ABCMeta

from entities.character import Character
from entities.enums.races import Races


class AbstractRaceBuilder(metaclass=ABCMeta):
    _race: Races

    @abstractmethod
    def apply_race(self, character: Character) -> Character:
        ...


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


class BaseElfBuilderMixin:

    def _apply_default(self, character: Character) -> None:
        character.wisdom.skills.perception.proficiency = character.proficiency
        character.speed = 30


class ElfBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.elf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.dexterity.increment_points(2)
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
