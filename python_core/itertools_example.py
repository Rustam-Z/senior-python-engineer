# advanced iteration functions in the itertools package

import itertools


def example_function(x):
    return x < 40


def main():
    # cycle b_iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))  # Joe
    print(next(cycle1))  # John
    print(next(cycle1))  # Mike
    print(next(cycle1))  # Joe

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))  # 100
    print(next(count1))  # 110
    print(next(count1))  # 120

    # accumulate creates an b_iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))  # [10, 20, 30, 40, 50, 50, 50]

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))  # ['A', 'B', 'C', 'D', '1', '2', '3', '4']

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(example_function, vals)))  # [40, 50, 40, 30]
    print(list(itertools.takewhile(example_function, vals)))  # [10, 20, 30]


if __name__ == "__main__":
    main()
