"""
Interface Segregation Principle
- Make fine-grained interfaces that are client-specific.
 Clients should not be forced to implement interfaces they do not use.
- The interface segregation principle states that an interface should be as small a possible in terms of cohesion.
In other words, it should do ONE thing.
- In OOP, an interface is a set of methods an object must-have.
"""
from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


class Car(Movable):
    def go(self):
        print("Going")


class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


def main():
    car = Car()
    car.go()

    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()


if __name__ == "__main__":
    main()
