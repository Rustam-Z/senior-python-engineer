"""
1. https://www.youtube.com/watch?v=vBH6GRJ1REM
2. https://www.geeksforgeeks.org/understanding-python-dataclasses/
3. https://realpython.com/python-data-classes/
4. https://docs.python.org/3/library/dataclasses.html
"""

import inspect
from pprint import pprint
from dataclasses import dataclass, field, astuple, asdict
from typing import List, Dict, Any


@dataclass(frozen=True, order=True)
class Comment:
    """A comment."""
    id: int = field()
    text: str = field(default="")  # Default value is set like this
    # We don't want all instances sharing the same list, so we use field(default_factory=list)
    replies: List[str] = field(default_factory=list, compare=False, hash=False, repr=False)


def menu():
    comment = Comment(id=1, text="This is a comment")
    print(comment)
    print(asdict(comment))
    print(astuple(comment))
    # pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == "__main__":
    menu()
