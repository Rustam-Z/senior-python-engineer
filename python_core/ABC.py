from abc import (
    ABC,
    abstractmethod,
)
from collections import namedtuple


class BasicPokemon(ABC):
    def __init__(self, name):
        self.name = name
        self._level = 1

    @abstractmethod
    def main_attack(self):
        ...

    def test(self):
        ...


Attack = namedtuple('Attack', ('name', 'damage'))


class Pikachu(BasicPokemon):
    def main_attack(self):
        return Attack('Thunder Shock', 5)


class Charmander(BasicPokemon):
    def main_attack(self):
        return Attack('Flame Thrower', 5)


p1 = Pikachu("Name")
print(p1.main_attack())