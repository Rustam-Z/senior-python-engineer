class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        if not isinstance(other, ImmutablePoint):
            return False
        return self._x == other._x and self._y == other._y


if __name__ == '__main__':
    ip = ImmutablePoint(10, 20)
    ip2 = ImmutablePoint(10, 20)

    print(ip.x, ip.y)
    print(ip == ip2)  # True
    print(ip is ip2)  # False

    # Since they are hashable, we can also use these objects as keys in a dictionary
    d = {ip: 'hello'}

    print(d)
    print(d[ip])
    print(d[ip2])
