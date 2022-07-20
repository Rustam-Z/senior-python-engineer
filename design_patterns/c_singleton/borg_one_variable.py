from typing import Dict


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


def main():
    """
    >>> rm1 = YourBorg()
    >>> rm2 = YourBorg()
    >>> rm1.state = 'Idle'
    >>> rm2.state = 'Running'
    >>> print('rm1: {0}'.format(rm1))
    rm1: Running
    >>> print('rm2: {0}'.format(rm2))
    rm2: Running
    # When the `state` attribute is modified from instance `rm2`,
    # the value of `state` in instance `rm1` also changes
    >>> rm2.state = 'Zombie'
    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie
    # Even though `rm1` and `rm2` share attributes, the instances are not the same
    >>> rm1 is rm2
    False
    # New instances also get the same shared state
    >>> rm3 = YourBorg()
    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie
    >>> print('rm3: {0}'.format(rm3))
    rm3: Zombie
    # A new instance can explicitly change the state during creation
    >>> rm4 = YourBorg('Running')
    >>> print('rm4: {0}'.format(rm4))
    rm4: Running
    # Existing instances reflect that change as well
    >>> print('rm3: {0}'.format(rm3))
    rm3: Running
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
