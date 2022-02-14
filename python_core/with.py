import contextlib


@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('finished')


with my_context() as foo:  # we use 'as' cuz my_context kind of returns yield 42
    print(f'foo is {foo}')  # foo is 42
