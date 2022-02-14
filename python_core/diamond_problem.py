
class Parent:
    def __init__(self):
        self.a = 2
        self.b = 4

    def print_name(self):
        print("parent")

    def form1(self):
        print("calling parent form1")
        print('p', self.a + self.b)


class Child1(Parent):
    def __init__(self):
        super().__init__()
        self.a = 50
        self.b = 4

    def print_name(self):
        print("child1")

    def print_super_name(self):
        super().print_name()

    def form1(self):
        print('bye', self.a - self.b)

    def callchildform1(self):
        print("calling parent from child1")
        super().form1()


class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.a = 3
        self.b = 4

    def print_name(self):
        print("child2")

    def form1(self):
        print('hi', self.a * self.b)

    def callchildform1(self):
        print("calling parent from child2")
        super().form1()


class Grandchild(Child1, Child2):
    def __init__(self):
        super().__init__()
        self.a = 10
        self.b = 4

    def print_name(self):
        print("grandchild")

    def print_super_name(self):
        super().print_name()

    def print_super_super_name(self):
        super().print_super_name()

    def callingparent(self):
        super().form1()


g = Grandchild()
print("When I print the name of my class it is:")
g.print_name()
print("When I print my superclass name, it is:")
g.print_super_name()
print("When I print the name of the superclass of my superclass, it is:")
g.print_super_super_name()
print("When you call methods on me, they will be executed from my class and my parent classes in the following order:")
print(Grandchild.__mro__)
g.form1()
g.callchildform1()
g.callingparent()
