"""
Abstract factory
Concrete factory

Abstract method
Concrete method
"""


class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """Abstract Factory"""

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """

        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the objects returned by the DogFactory """

        pet = self.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is '{pet}'!")
        print(f"Our pet says hello by '{pet.speak()}'")
        print(f"Its food is '{pet_food}'!")


if __name__ == "__main__":
    # Create a Concrete Factory
    factory = DogFactory()

    # Create a pet store housing our Abstract Factory
    shop = PetStore(factory)

    # Invoke the utility method to show the details of our pet
    shop.show_pet()
