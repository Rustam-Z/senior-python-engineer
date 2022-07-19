"""
It allows a client to have sequential access to the elements of an aggregate object (without exposing its underlying structure).

Composite related to iterator.
"""


def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number

    # Let's test the generator returned by our iterator


for num in count_to(7):
    print(num)



