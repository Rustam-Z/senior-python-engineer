import enum


# Creating enumerations using class
@enum.unique
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
    python = enum.auto()


print(Animal.dog)  # Animal.dog
print(type(Animal.dog))  # <enum 'Animal'>
print(repr(Animal.dog))  # <Animal.dog: 1>

print(Animal(2))  # Animal.cat
print(Animal['lion'])  # Animal.lion

# Assigning enum member
mem = Animal.dog
print(mem.value)  # 1
print(mem.name)  # dog

# ENUMs are hashable and can be used a key to a dictionary
sample = {Animal.dog: "Bobik"}
print(sample)  # {<Animal.dog: 1>: 'Bobik'}

# Comparison using "is"
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

# Comparison using "!="
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")
