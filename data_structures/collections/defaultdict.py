"""
collections.defaultdict – Return Default Values for Missing Keys
https://realpython.com/python-defaultdict/

Best use cases with:
1. List
2. Set
3. int, for counting
"""

from collections import defaultdict


def example_with_list():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d.items())


def example_with_int():
    """Counter"""
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print(d.items())


def example_with_set():
    s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)
    print(d.items())


def main():
    example_with_list()
    example_with_int()
    example_with_set()


if __name__ == '__main__':
    main()
