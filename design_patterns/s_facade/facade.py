"""
Facade provides a simplified yet limited interface to decrease the complexity of an application.
Complex subsystems with multiple moving parts could be “masked” by Facade.

Use case. Create the Facade class in case you work with complex libraries & APIs and you need only the part of their functionality.

+ System complexity is separated from the code
- Using the Facade pattern, you can create a god object.

https://jellyfish.tech/blog/implementation-of-common-design-patterns-in-python/
"""


class Addition:
    def __init__(self, field1: int, field2: int):
        self.field1 = field1
        self.field2 = field2

    def get_result(self):
        return self.field1 + self.field2


class Multiplication:
    def __init__(self, field1: int, field2: int):
        self.field1 = field1
        self.field2 = field2

    def get_result(self):
        return self.field1 * self.field2


class Subtraction:
    def __init__(self, field1: int, field2: int):
        self.field1 = field1
        self.field2 = field2

    def get_result(self):
        return self.field1 - self.field2


class Facade:
    @staticmethod
    def make_addition(*args) -> Addition:
        return Addition(*args)

    @staticmethod
    def make_multiplication(*args) -> Multiplication:
        return Multiplication(*args)

    @staticmethod
    def make_subtraction(*args) -> Subtraction:
        return Subtraction(*args)


if __name__ == "__main__":
    addition_obj = Facade.make_addition(5, 5)
    multiplication_obj = Facade.make_multiplication(5, 2)
    subtraction_obj = Facade.make_subtraction(15, 5)

    print(addition_obj.get_result())
    print(multiplication_obj.get_result())
    print(subtraction_obj.get_result())
