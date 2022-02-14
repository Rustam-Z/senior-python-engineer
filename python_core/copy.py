# def f(x):
#     print("outer", x)
#     if x == 1:
#         print("inside if", x)
#         return x
#     else:
#         x -= 1
#         print("inner", x)
#         f(x)
#
#     print("asdfads")
#
# x = 2
# print(f(x), x)


# a = [[1,2,3]]
# b = a[:]
#
# print(id(a), id(b))
#
# b[0][0] = 999
#
# print(a, b)

import copy

old_list = [4, 5, 6, [2,3,3]]
new_list = copy.copy(old_list)

new_list[3] = [99999]

print(old_list, new_list)
