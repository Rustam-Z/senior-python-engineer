from functools import singledispatch


@singledispatch
def func(val):
    raise NotImplementedError


@func.register
def _(val: str):
    print('This is a string')


@func.register
def _(val: int):
    print('This is an int')


func("test")
func(1)
# func(None)


################

from multipledispatch import dispatch


@dispatch(int, int)
def Add(a, b):
    return a + b


@dispatch(int, int, int)
def Add(a, b, c):
    return a + b + c


@dispatch(int, int, int, int)
def Add(a, b, c, d):
    return a + b + c + d


print(Add(10, 10, 10))
