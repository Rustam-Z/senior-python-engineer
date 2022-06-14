# https://python-course.eu/oop/class-instance-attributes.php

def change_attribute(value):
    """In this function I can not access car.color directly"""
    Car.color = value


class Car:
    color = "green"


def main():
    car1 = Car()
    car2 = Car()
    # car1.color = "black"  # Bad code :)

    change_attribute("red")
    print(car1.color)  # Prints red
    print(car2.color)  # Prints red

    change_attribute("blue")
    print(car1.color)  # Prints blue
    print(car2.color)  # Prints blue


class C:
    counter = 0

    def __init__(self):
        C.counter += 1

    def __del__(self):
        type(self).counter -= 1


def main2():
    x = C()
    print("Number of instances: " + str(C.counter))  # 1
    y = C()
    print("Number of instances: " + str(C.counter))  # 2
    del x
    print("Number of instances: " + str(C.counter))  # 1
    del y
    print("Number of instances: " + str(C.counter))  # 0


if __name__ == "__main__":
    main()
    main2()
