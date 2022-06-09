class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


animals = [
    Animal('lion'),
    Animal('mouse')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')


animal_sound(animals)


"""
If we don't follow OCP then we could have one function with many if elses for all type of animals.
And if we add the new animal we must edit that function.

Like following:
"""


animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)
