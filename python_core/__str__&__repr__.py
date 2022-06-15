"""
Class String Functions

object.__str__(self) -> str(object), print(object), "{0}".format(object)
object.__repr__(self) -> repr(object)
object.__format__(self, format_spec) -> format(object, format_spec)
object.__bytes__(self) -> bytes(object)
"""


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2}>".format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


def main():
    # create a new Person object
    person = Person()

    # use different Python functions to convert it to a string
    print(repr(person))  # <Person Class - fname:Joe, lname:Marini, age:25>
    print(str(person))  # Person (Joe Marini is 25)
    print("Formatted: {0}".format(person))  # Formatted: Person (Joe Marini is 25)
    print(bytes(person))  # b'Person:Joe:Marini:25'

    print(person)  # Person (Joe Marini is 25)
    print(person.__str__())  # Person (Joe Marini is 25)
    print(person.__repr__())


if __name__ == "__main__":
    main()
