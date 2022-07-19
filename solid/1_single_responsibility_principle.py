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
from typing import List


class DjangoOrm:
    """This is the c_singleton class used to create a connection with DB."""
    def __init__(self, db_path: str):
        self.db_path = db_path

    def connect(self):
        return Connection()


@dataclass
class Animal:
    """
    Entity class.
    """
    name: str
    age: int
    category: str

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        if value not in ['mammal', 'bird', 'reptile']:
            raise ValueError('Invalid category')
        self._category = value


class AnimalRepository:
    """
    DAO - Data Access Object.
    Responsible for storing data into database.
    It is good to make it interface, and inherit PROD and TEST classes from it.
    """

    def __init__(self, database: DjangoOrm):
        self.database = database

    def save(self, animal: Animal) -> bool:
        """If save is successful, save() returns True, else False."""
        ...

    def get(self, name: str) -> Animal:
        ...

    def delete(self, name: str) -> bool:
        """If delete is successful, save() returns True, else False."""
        ...

    def update(self, animal: Animal) -> bool:
        """If update is successful, save() returns True, else False."""
        ...


class AnimalBusinessLogic:
    """
    DTO - Data Transfer Object.
    BusinessLogic - responsible for business logic.
    """

    def __init__(self, animal_repository: AnimalRepository):
        self.animal_repository = animal_repository

    def get_animals_by_age(self) -> List[Animal]:
        ...

    def get_average_age_by_category(self, category: str) -> List[Animal]:
        ...


if __name__ == "__main__":
    orm = DjangoOrm("the_path_to_db").connect()  # It should be c_singleton because many repositories will use the same database.
    animal_repository = AnimalRepository(orm)
    animal_business_logic = AnimalBusinessLogic(animal_repository)
    animal = Animal(name="Bobik", age=5, category='mammal')  # Create an animal.
    animal_repository.save(animal)  # Save it into database.
    animals_list = animal_business_logic.get_animals_by_age()  # Get all animals by age.
