"""
Factory Pattern is useful when you are not sure which types of objects you need in your system
"""


class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


if __name__ == "__main__":
    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    print(c.speak())
