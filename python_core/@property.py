class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected String!")
        self._name = value


person1 = Person("Rustam")

print(person1.name)

person1.name = "Rustam-Z"

print(person1.name)

person1.name = 2

print(person1.name)