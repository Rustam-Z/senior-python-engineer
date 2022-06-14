class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


if __name__ == '__main__':
    members = {
        Person('John', 22),
        Person('Jane', 22)
    }
    print(type(members))  # set
    print(members)  # Only 1 object because in eq() we compare ages only

