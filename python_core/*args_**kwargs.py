def foo(required, *args, **kwargs):
    print(required)
    if args:
        print("args", args)
    if kwargs:
        print("kwargs", kwargs)
    print("\n")


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def recv(maxsize, *, block):
    # Receives a message
    pass


def combined_example(pos_only, /, standard, *, kwd_only):
    print("p", pos_only, "s", standard, "k", kwd_only)


if __name__ == "__main__":
    # Example 1
    foo('hello')
    foo("hello", 1, 2, 3, key1='value', key2=999)

    # Example 2
    kwd_only_arg(1, 2, 3, arg="Hello")  # TypeError: function takes 0 positional arguments but 3 positional arguments
    kwd_only_arg(arg="Test", another_arg="Test 2")  # TypeError
    kwd_only_arg(arg="Test")  # This works

    # Example 3
    pos_only_arg(1, 2, 3, 44)  # TypeError
    pos_only_arg(1)  # This works

    # Example 4
    recv(1024, True)  # TypeError, only 1 positional arg.
    recv(1024, block=True)  # Correct

    # Example 5
    combined_example(1, 2, kwd_only=3)  # p 1 s 2 k 3
    combined_example(1, standard=2, kwd_only=3)  # p 1 s 2 k 3
