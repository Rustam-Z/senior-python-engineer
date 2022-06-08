"""
types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries
"""

from types import MappingProxyType

read_only = MappingProxyType({'one': 1, 'two': 2})
print(read_only['one'])

read_only['one'] = 23  # Raises a TypeError
print(read_only['one'])

