"""
Separating class from building complex object.
Separating actual algorithm of creation of objects from actual object being created.

Builder constructs/initializes object.
Director knows how construct, concrete algorithm.

Director
    .construct() -> open_file, parse_config, build_product, close_file
Builder
    .open_file()
    .parse_config()
    .build_product()
    .close_file()

ConcreteBuilder * concreteBuilder = new ConcreteBuilder();
Director * director = new Director(ConcreteBuilder);
director->construct("myAssets.zip");
Product * product = concreteBuilder.getProduct();

Isn't is wonderful! Wow!

https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py
https://youtu.be/VCxNt2K7aVY?t=527
"""
from typing import Type


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


class Director:
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()


class Builder:
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

    def get_car(self) -> Type[Car]:
        """Get object method should be inside Concrete Builder method.
        Otherwise, we will lose all butty of Builder design pattern."""
        return self.car


if __name__ == "__main__":
    concrete_builder = SkyLarkBuilder()
    director = Director(concrete_builder)
    director.construct()
    car = concrete_builder.get_car()
    print(car)  # Skylark | Regular tires | Turbo engine
