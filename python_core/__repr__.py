class Test:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Test({self.data})"

    def __str__(self):
        return "Test class with data = " + str(self.data)


if __name__ == '__main__':
    test_object = Test(1)

    print(repr(test_object))
    print(str(test_object))
    print(test_object)
