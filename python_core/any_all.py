def check_any_all():
    """
    any() returns True if ang of the sequence value is True
    """
    list_ = [1, 2, 3, 4, 5, 0]
    print(any(list_))  # True
    print(all(list_))  # False


if __name__ == '__main__':
    check_any_all()
