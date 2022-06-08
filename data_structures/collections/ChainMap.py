"""
collections.ChainMap – Search Multiple Dictionaries as a Single Mapping
"""

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

chain = ChainMap(dict1, dict2)
print(chain)  # ChainMap({'a': 1, 'b': 3}, {'b': 2, 'c': 4})
print(list(chain))  # ['b', 'c', 'a']
print(chain['b'])  # 2
