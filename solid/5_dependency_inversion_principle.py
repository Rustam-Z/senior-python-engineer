"""
Dependency Inversion Principle
- High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.

Use the dependency inversion principle to make your code more robust by making the high-level module dependent on the abstraction, not the concrete implementation.

Dependency Injection is an implementation technique for populating instance variables of a class.
Dependency Inversion is a general design guideline which recommends that classes should only have direct relationships with high-level abstractions.
"""


from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 2


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


def main():
    # FXConverter
    converter = FXConverter()
    app = App(converter)
    app.start()

    # AlphaConverter
    converter = AlphaConverter()
    app = App(converter)
    app.start()


if __name__ == '__main__':
    main()
