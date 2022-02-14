"""
Covering Your A** With Assertions

Tip!
It is a good practice to use the assert statement for debugging purpose.

Important!
Do not use assert with tuple in Python.
"""

assert 1 == 1  # Will not produce the error
assert 1 == '1', '1 should be integer'  # Will produce AssertionError: 1 should be integer
