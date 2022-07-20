"""
Here the problem is that Korean has speak_korean() but British has speak_english().
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


def main():
    objects = []  # List to store speaker objects

    korean = Korean()
    british = British()

    objects.append(Adapter(korean, speak=korean.speak_korean))  # Later speak() will be used to access the speak_korean
    objects.append(Adapter(british, speak=british.speak_english))

    # print(Adapter(korean, speak=korean.speak_korean).original_dict())

    for obj in objects:
        print(f"{obj.name} says {obj.speak()}")


if __name__ == "__main__":
    main()
