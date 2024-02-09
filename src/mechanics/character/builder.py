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

    def _apply_default(self, character: Character):
        character.wisdom.skills.perception.proficiency = character.proficiency


class ElfBuilder(AbstractRaceBuilder, BaseElfBuilderMixin):
    _race = Races.elf

    def apply_race(self, character: Character) -> Character:
        self._apply_default(character)
        character.dexterity.increment_points(2)
        character.speed = 30
        return character

