"""
collections.OrderedDict – Remember the Insertion Order of Keys
"""

import collections

d = collections.OrderedDict(four=4, one=1, two=2, three=3)
print(d)  # OrderedDict([('four', 4), ('one', 1), ('two', 2), ('three', 3)])

d['five'] = 5
print(d)  # OrderedDict([('four', 4), ('one', 1), ('two', 2), ('three', 3), ('five', 5)])
