"""
Class Attribute Functions

object.__getattribute__(self, attr) is invoked before looking at the actual attributes on the object.
object.__getattr__(self, attr) is only invoked if the attribute wasn't found the usual ways
object.__setattr__(self, attr, val) -> object.attr = val
object.__delattr__(self, attr) -> del object.attr
object.__dir__(self) -> dir(object)

https://stackoverflow.com/questions/3278077/difference-between-getattr-and-getattribute
https://www.linkedin.com/learning/advanced-python/computed-attributes?autoSkip=true&autoplay=true&resume=false&u=2113185
"""


def example1():
    # We will try to access the attribute which doesn't exist in class, and AttributeError will be raised.
    class Count:
        def __init__(self, mymin, mymax):
            self.mymin = mymin
            self.mymax = mymax

    obj1 = Count(1, 10)
    print(obj1.mymin)
    print(obj1.mymax)
    # print("Not existing:", obj1.mycurrent)  # AttributeError: 'Count' object has no attribute 'mycurrent'


def example2():
    # The same example with __getattr__, python will create a new attribute and assign it to 0
    class Count:
        def __init__(self, mymin, mymax):
            self.mymin = mymin
            self.mymax = mymax

        def __getattr__(self, item):
            self.__dict__[item] = 0
            return 0

    obj1 = Count(1, 10)
    print(obj1.mymin)
    print(obj1.mymax)
    print("Not existing:", obj1.mycurrent1)  # Will not raise an exception


def example3():
    # The same example with getattribute
    # If both methods are used, exception will be ignored by getattr
    class Count:
        def __init__(self, mymin, mymax):
            self.mymin = mymin
            self.mymax = mymax
            self.current = None

        def __getattribute__(self, item):
            if item.startswith('cur'):
                raise AttributeError("Don't try to access attributes starting with 'cur'")
            return super().__getattribute__(item)
            # or you can use -> return object.__getattribute__(self, name)

    obj1 = Count(1, 10)
    print(obj1.mymin)
    print(obj1.mymax)
    print(obj1.current)  # AttributeError: Don't try to access attributes starting with 'cur'


def example4():
    class MyColor:
        def __init__(self):
            self.red = 50
            self.green = 75
            self.blue = 100

        # use getattr to dynamically return a value
        def __getattr__(self, attr):
            if attr == "rgbcolor":
                return self.red, self.green, self.blue
            elif attr == "hexcolor":
                return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
            else:
                raise AttributeError

        # use setattr to dynamically return a value
        def __setattr__(self, attr, val):
            if attr == "rgbcolor":
                self.red = val[0]
                self.green = val[1]
                self.blue = val[2]
            else:
                super().__setattr__(attr, val)

        # use dir to list the available properties
        def __dir__(self):
            return "rgbolor", "hexcolor"

    # create an instance of myColor
    cls1 = MyColor()
    # print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # access a regular attribute
    print(cls1.red)

    # list the available attributes
    print(dir(cls1))


def main():
    # example1()
    # example2()
    # example3()
    example4()


if __name__ == "__main__":
    main()
