"""
Duck typing in Python.

Using Duck Typing, we do not check types at all.
Instead, we check for the presence of a given method or attribute.
"""


class Duck:

    def __init__(self, name):
        self.name = name

    def quack(self):
        print('Quack!')


class Car:

    def __init__(self, model):
        self.model = model

    def quack(self):
        print('I can quack, too!')


def quacks(obj):
    obj.quack()


def main():
    donald = Duck('Donald Duck')
    car = Car('Tesla')
    quacks(donald)
    quacks(car)


if __name__ == "__main__":
    main()
