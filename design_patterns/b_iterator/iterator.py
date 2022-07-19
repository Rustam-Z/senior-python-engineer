"""
Iterator allows traversing the elements of collections without exposing the internal details.

+ Clean client code (Single Responsibility Principle).
+ Introducing iterators in collections is possible without changing the client’s code (Open/Closed Principle).
+ Each iteration object has its own iteration state, so you can delay & continue iteration.
- Use of iterators with simple collections can overload the application.
"""

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection,
                 reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration
        return value


class WordsCollection(Iterable):
    def __init__(self, collection=None):
        if collection is None:
            collection = []
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection_ = WordsCollection()
    collection_.add_item("First")
    collection_.add_item("Second")
    collection_.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection_))

    print("Reverse traversal:")
    print("\n".join(collection_.get_reverse_iterator()))
