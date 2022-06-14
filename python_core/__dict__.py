class MyClass(object):
    class_var = 1

    def __init__(self, instance_var):
        self.instance_var = instance_var


if __name__ == '__main__':
    foo = MyClass(2)
    bar = MyClass(3)

    foo.__dict__['instance_var'] = 53355353

    print(vars(MyClass))
    print(MyClass.__dict__)

    print(foo.__dict__)
    print(bar.__dict__)
