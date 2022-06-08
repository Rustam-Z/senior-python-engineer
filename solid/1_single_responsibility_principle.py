"""
Single Responsibility Principle
- A class should have only one reason to change.

Let's say we have a class that has 3 responsibilities:
- Creates a new entity (e.g. a class)
- Stores data into database
- Includes business logic
It is not a good idea to have all three responsibilities in one class. In the future we can change our database or business logic.
And we don't want to touch a class that is responsible for creating an entity.

So, we should split the class into 3 classes:
- A class that creates an entity
- A class that stores data into database
- A class that includes business logic
"""
from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    age: int
    category: str

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in ['mammal', 'bird', 'reptile']:
            raise ValueError('Invalid category')
        self._category = value


if __name__ == "__main__":
    # Create an animal
    animal = Animal(name="Bobik", age=5, category='mammal')
    print(animal)




