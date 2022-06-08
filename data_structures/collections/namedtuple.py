"""
collections.namedtuple – Convenient Data Objects, assigning meaning to each position at tuple
typing.NamedTuple – Improved Namedtuples, with type hints and more

somenamedtuple._make(iterable) – Constructs a namedtuple from a sequence or iterable
somenamedtuple._asdict() – Returns a new OrderedDict which maps field names to their values
somenamedtuple._replace(**kwargs) – Returns a new namedtuple replacing specified fields with new values
somenamedtuple._fields – Returns the list of field names
"""

from collections import namedtuple


def example_1():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)
    print(p.x, p.y)
    print(p.x + p.y)
    # p.z = 234  # AttributeError: 'Point' object has no attribute 'z'


def example_2():
    """Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3:
    """
    EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

    import csv
    for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
        print(emp.name, emp.title)

    import sqlite3
    conn = sqlite3.connect('/companydata')
    cursor = conn.cursor()
    cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
    for emp in map(EmployeeRecord._make, cursor.fetchall()):
        print(emp.name, emp.title)


def main():
    example_1()


if __name__ == "__main__":
    main()
