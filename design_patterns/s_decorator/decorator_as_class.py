class my_decorator:
    def __init__(self, func):
        print("inside my_decorator.__init__()")
        self.function = func

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)  # Prove that function definition has completed
        print("inside my_decorator.__call__() that returns", result)


@my_decorator
def my_function(name, message='Hello'):
    print("{}, {}".format(message, name))
    return 49


if __name__ == "__main__":
    my_function("Rustam")
