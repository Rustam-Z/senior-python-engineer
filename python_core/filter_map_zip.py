# use transform functions like sorted, filter, map


def filter_func(x):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x**2


def to_grade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    odds = list(filter(filter_func, nums))
    print(odds)  # [1, 5, 13, 381, 47]

    # use filter on non-numeric sequence
    lowers = list(filter(filter_func2, chars))
    print(lowers)  # ['a', 'b', 'c', 'e', 'i', 'k', 'l', 'm', 'n', 'o']

    # use map to create a new sequence of values
    squares = list(map(square_func, nums))
    print(squares)  # [1, 64, 16, 25, 169, 676, 145161, 168100, 3364, 2209]

    # use sorted and map to change numbers to grades
    grades_sorted = sorted(grades)
    letters = list(map(to_grade, grades_sorted))
    print(grades_sorted, letters)  # [61, 66, 74, 78, 81, 89, 94, 99] ['F', 'D', 'C', 'C', 'B', 'B', 'A', 'A']

    # zip grades and letters
    zipped = zip(grades_sorted, letters)
    print(list(zipped))  # [(61, 'F'), (66, 'D'), (74, 'C'), (78, 'C'), (81, 'B'), (89, 'B'), (94, 'A'), (99, 'A')]


if __name__ == "__main__":
    main()
