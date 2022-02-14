class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 2


t = Test()
t._bar = 43

print(t.__dict__)

