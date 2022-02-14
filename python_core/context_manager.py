"""
'with' statement

It helps simplify some common resource management patterns by abstracting their functionality.

__enter__ __exit__

@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('finished')

with my_context() as foo:
    print(f'foo is {foo}') # foo is 42
"""

from contextlib import contextmanager


class ManagedFile:
    """
    Class based context manager
    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


@contextmanager
def managed_file(name):
    """
    Generator based context manager.
    :param name:
    :return:
    """
    try:
        file = open(name, 'w')
        yield file
    finally:
        file.close()
        print("Finished")


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)

    def wow(self, text):
        # Works the same as print
        print(' ' * self.level + text)


if __name__ == "__main__":
    with ManagedFile('hello.txt') as f:
        f.write('hello, world!\n')
        f.write('bye now')

    with managed_file("hello2.txt") as f:
        f.write('hello, world!\n')
        f.write('bye now')

    with Indenter() as indent:
        indent.wow('hi!')
    with indent:
        indent.wow('hello')
        with indent:
            indent.wow('bonjour')
    indent.wow('hey')