"""
Provides a way to encapsulate a group of individual factories.
Creates object without specifying their actual class.

In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.
"""

from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetStore:
    """Abstract Factory"""
    def __init__(self, pet_factory: Type[Pet]) -> None:
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def buy_pet(self, name: str) -> Pet:
        """Creates and shows a pet using the abstract factory"""
        pet = self._pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet


if __name__ == "__main__":
    cat_store = PetStore(Cat)

    pet = cat_store.buy_pet("Lucy")  # Here is your lovely Cat<Lucy>
    pet.speak()  # meow
