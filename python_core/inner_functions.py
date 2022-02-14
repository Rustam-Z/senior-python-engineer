
def make_adder(x):
    def add(n):
        return x + n
    return add


plus_3 = make_adder(3)
print(plus_3(10))
