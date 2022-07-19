"""
Open Closed Principle
- Software entities (classes, modules, functions) should be open for extension, but closed for modification.
- Don't check for object type, don't use if/else, but use Polymorphism instead.

https://www.youtube.com/watch?v=aWAmScEixoE
https://www.pythontutorial.net/python-oop/python-open-closed-principle/
https://github.com/heykarimoff/solid.python/blob/master/2.ocp.py

If you want to add new features in the future, you should implement the abstract class.
In our example, Animal class is abstract, it is open for extensions such as Snake, Lion and Mice.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        ...

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Lion(Animal):
    def make_sound(self) -> str:
        return 'roar'


class Mouse(Animal):
    def make_sound(self) -> str:
        return 'squeak'


class Snake(Animal):
    def make_sound(self) -> str:
        return 'hiss'


def get_animal(name: str) -> Animal:
    """The c_factory method"""
    animals = dict(dog=Lion("Asad"), cat=Mouse("Nizo"), snake=Snake("Rust"))
    return animals[name]


# It is the function where show how to use OCP
def animal_sound(animal: Animal):
    return animal.make_sound()


def main():
    animal = get_animal("snake")
    print(animal_sound(animal))


if __name__ == "__main__":
    main()

