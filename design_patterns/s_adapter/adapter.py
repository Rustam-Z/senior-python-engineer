"""
Adapter pattern - making the incompatible objects adaptable to each other.
by converting the interface of a class into another one that a client is expecting

Problem:
- Interface incompatible between client and server.

Scenario:
- Korean: speak_Korean()
- English: speak_English()
- Client needs uniform interface: speak()

Solution:
- Adapter pattern to translate the method names between server and client.

Bridge and decorator related to Adapter pattern.
"""


class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, adapter_object, **adapted_method):
        """Change the name of the method"""
        self._object = adapter_object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the
        # concrete method For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)

    def original_dict(self):
        """Print original object dict"""
        return self._object.__dict__


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

# print(Adapter(korean, speak=korean.speak_korean).original_dict())

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
