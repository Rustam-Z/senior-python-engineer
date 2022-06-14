import copy


def example():
    """
    It is not the copying example, b = a creates a new name in namespace which point to one object.
    """
    a = [1, 2]
    b = a
    b[0] = "Both will be changed"
    print(a, b)


def example1():
    a = [[1,2,3]]
    b = a[:]

    print(id(a), id(b))  # Different ids

    b[0][0] = 999

    print(a, b)  # But both will be changed, because [:] is shallow copy


def example1_with_deepcopy():
    a = [[1,2,3]]
    b = copy.deepcopy(a)

    print(id(a), id(b))  # Different ids

    b[0][0] = 999

    print(a, b)  # Only b will be changed


def example2():
    old_list = [4, 5, 6, [2,3,3]]
    new_list = copy.copy(old_list)

    new_list[3] = [99999]

    print(old_list, new_list)  # Only new_list will be changed


if __name__ == '__main__':
    example()
    example1()
    example1_with_deepcopy()
    example2()
