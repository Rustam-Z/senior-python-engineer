"""
Strategy pattern - we have a default method, we can change its behaviour with another function at run time.

It is easy to implement with Python with its build-in "types" module.
"""


import types


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another strategy is provided.
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()

