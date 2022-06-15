"""
Class Comparison Operators = Special methods to compare objects to each other

object.__gt__(self, other) -> self > other
object.__ge__(self, other) -> self >= other
object.__lt__(self, other) -> self < other
object.__le__(self, other) -> self <= other
object.__eq__(self, other) -> self == other
object.__ne__(self, other) -> self != other
"""


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


def main():
    # define some employees
    dept = [
        Employee("Tim", "Sims", 5, 9),
        Employee("John", "Doe", 4, 12),
        Employee("Jane", "Smith", 6, 6),
        Employee("Rebecca", "Robinson", 5, 13),
        Employee("Tyler", "Durden", 5, 12)
    ]

    # Who's more senior?
    print(bool(dept[0] > dept[2]))  # False, because 5 < 6
    print(bool(dept[4] < dept[3]))  # True, because 12 < 13

    # sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


if __name__ == "__main__":
    main()
