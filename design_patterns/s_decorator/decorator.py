"""
Decorator attaches new behaviors to the objects without modifying their structure.

+ Changes the object behavior without creating a subclass.
+ You can combine several behaviors by wrapping an object into multiple decorators.

Problem:
- Add new feature to an existing object
- Dynamic changes
- Without subclasses

Solution:
- Built-in decorator
"""

from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator(*args, **kwargs):
        # Grab the return value of the function being decorated
        ret = function(*args, **kwargs)

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here!
@make_blink
def hello_world():
    """Original function! """
    return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)
