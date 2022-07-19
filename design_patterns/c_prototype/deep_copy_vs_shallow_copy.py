import copy


def print_xy(xs, ys):
    print(">>> xs", xs)
    print(">>> ys", ys)


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ys = copy.deepcopy(xs)  # Make a shallow copy

print_xy(xs, ys)

ys.append(['new sublist'])

print_xy(xs, ys)

ys[1][0] = 'X'

print_xy(xs, ys)

