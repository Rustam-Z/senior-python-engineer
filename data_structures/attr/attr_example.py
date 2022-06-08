"""
Compared to dataclass where we can describe the attributes of the class, like:
@dataclass
class Comment:
    id: int
    text: str

In attr, we can't use that syntax, we must use attr.ib() always:
@attr.dataclass
class Comment:
    id: attr.ib(type=int)
    text: attr.ib(type=str)
OR
@attr.s
class Comment:
    id: int = attr.ib()
    text: str = attr.ib()

Moreover, if one of the attributes uses attr.ib(), then all of them must use attr.ib().
And we can't specify default value like: id: int = 123
"""

import inspect
from pprint import pprint
from typing import List, Dict, Any
import attr


@attr.s(order=True, slots=True)  # dataclass doesn't support slots
class Comment:
    """A comment."""
    id: int = attr.ib(validator=attr.validators.instance_of(int))
    text: str = attr.ib(default="", converter=str)
    replies: List[str] = attr.ib(factory=list, order=False, hash=False, repr=False)


def main():
    comment = Comment(id=1, text="This is a comment", replies=["reply1", "reply2"])
    print(comment)
    print(attr.asdict(comment))
    print(attr.astuple(comment))
    # pprint(inspect.getmembers(Comment, inspect.isfunction))
    # comment.testing_slots = "testing"  # throws AttributeError


if __name__ == "__main__":
    main()
