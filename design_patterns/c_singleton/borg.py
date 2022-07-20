"""
Singleton is used when you want to allow only one object to be instantiated from a class.

Borg pattern making the class attributes global.
There are multiple instances that share the same state.
Sharing state instead of sharing instance.
"""


class Borg:
    _shared_data = {}  # Class attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):
    """This class now shares all its attributes among its various instances.
    This essentially makes the singleton objects an object-oriented global variable.
    """
    def __init__(self, **kwargs):
        super().__init__()  # Borg.__init__(self)
        self._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary for printing


if __name__ == "__main__":
    # Let's create a singleton object and add our first acronym
    x = Singleton(HTTP="Hyper Text Transfer Protocol")

    print(x)

    # Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
    y = Singleton(SNMP="Simple Network Management Protocol")

    print(y)
