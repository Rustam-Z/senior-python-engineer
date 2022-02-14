# def decorator(func):
#     test = func()
#     return test + " Rustam"
#
#
# def hello():
#     return "Hello"
#
#
# hello = decorator(hello)
#
# print(hello)


############################################################################

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = my_decorator(say_whee)
# say_whee()

############################################################################

#
# def do_twice(func):
#     def wrapper_do_twice(name):
#         func(name)
#         func(name)
#     return wrapper_do_twice
#
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# # greet("Rustam")
#
#
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
# s = return_greeting("Adam")

