print("Hello from Global score")


class Test:
    print("Hello from class")

    def __new__(cls, *args, **kwargs):
        print("Hello from new()")

    def __init__(self, attr):
        print("Hello from init()")
        self.attr = attr


if __name__ == '__main__':
    print("Hello from main")
    test = Test("Testing...")

    """RESULT:
    Hello from Global score
    Hello from class
    Hello from main
    Hello from new()
    """
