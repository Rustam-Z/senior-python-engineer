# def mygenerator():
#     print('First item')
#     yield 10
#
#     print('Second item')
#     yield 20
#
#     print('Last item')
#     yield 30
#
#
# gen = mygenerator()
# next(gen)
# next(gen)
# next(gen)

############################################################

# def coroutine():
#     for i in range(1, 10):
#         print("From generator {}".format((yield i)))
#
#
# c = coroutine()
# print(type(c))
# c.send(None)
# try:
#     while True:
#         print("From user {}".format(c.send(1)))
# except StopIteration:
#     pass


def echo():
    while True:
        val = (yield)
        yield val


g = echo()
next(g)  # move to 1st yield
print(g.send(2))  # execution stops at 2nd yield

next(g)  # execution stops at 1st yield
print(g.send(3))  # execution stops at 2nd yield
############################################################
#
# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return True
#     else:
#         return False
#
#
# def infinite_palindromes():
#     num = 0
#     while True:
#         if is_palindrome(num):
#             i = (yield num)
#             if i is not None:
#                 num = i
#         num += 1
#
#
# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     print(i)
#     digits = len(str(i))
#     if digits == 5:
#         pal_gen.throw(ValueError("We don't like large palindromes"))
#     pal_gen.send(10 ** (digits))
