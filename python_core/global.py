# x = 40

def outer():
    x = 30

    def f():
        global x
        """The global x statement indicates that while f() executes,
        references to the name x will refer to the x that is in the global namespace.
        """
        # This will modify global, same as ... globals()['x'] = 40
        x = 40
        print(x)

    f()

outer()
print(x)
