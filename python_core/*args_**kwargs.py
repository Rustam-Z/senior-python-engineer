def foo(required, *args, **kwargs):
    print(required)
    if args:
        print("args", args)
    if kwargs:
        print("kwargs", kwargs)
    print("\n")


if __name__ == "__main__":
    foo('hello')
    foo("hello", 1, 2, 3, key1='value', key2=999)
