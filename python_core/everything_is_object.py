# Example 1
def func():
    hello = "Hello"
    return hello


func.temp = 1

print(func.__dict__)

print(func)


# Example 2
class Point:
    __slots__ = "x", "y"  # Restricting number of attributes, and making memory consumption faster, compared to __dict__

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Example 3
"""
>>> class A:
...     def __init__(self, a):
...         self.a = a
... 
>>> a = A(4)
>>> a.__dict__
{'a': 4}
>>> a.f = 123
>>> a.__dict__  # Default is __dict__ but we can overwrite with __slots__
{'a': 4, 'f': 123}
>>> 
"""


# Example 4
class Circle(object):
    """Implementation-independent abstraction: for example, there could be a rectangle class!"""

    def __init__(self, radius, drawing_api):
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.test(self._radius)

    # def test2(self):
    #     """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
    #     self._drawing_api.test22 = "test"


c = Circle(5, "test")
c.draw()
