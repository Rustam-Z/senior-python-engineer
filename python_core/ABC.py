from abc import ABC, abstractmethod
from collections import namedtuple


class BasicPokemon(ABC):
    def __init__(self, name):
        self.name = name
        self._level = 1

    @abstractmethod
    def main_attack(self):
        ...

    def test_no_need_to_implement_non_abstract_method(self):
        ...


class Pikachu(BasicPokemon):
    def main_attack(self):
        return Attack('Thunder Shock', 5)


class Charmander(BasicPokemon):
    def main_attack(self):
        return Attack('Flame Thrower', 5)


if __name__ == '__main__':
    Attack = namedtuple('Attack', ('name', 'damage'))  # It is allowed because Python is interpreted language
    p1 = Pikachu("Name")
    print(p1.main_attack())
