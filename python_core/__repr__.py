class Test:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Repr " + str(self.data)

    def __str__(self):
        return "Str " + str(self.data)


test_object = Test(1)

print(repr(test_object))
print(str(test_object))
