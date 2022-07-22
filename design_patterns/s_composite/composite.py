"""
TREE Data Structure.
Describes a group of objects that is treated the same way as a single instance of the same type of the objects.

Problem:
- We have a Menu
- We have a Submenu for menu items

Solution:
- Component (Abstract class)
- Child (Concrete class), inherits from Component
- Composite (Concrete class), inherits from Component
    - child objects (to, from)
"""

from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def component_function(self):
        ...


class Child(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):
    """Concrete class and maintains the tree recursive structure"""
    def __init__(self, *args, **kwargs):
        # Component.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]  # First argument is the "name"

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print("{}".format(self.name))
        # print(self.children)  # Just for debugging purposes

        # Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


def main():
    # Submenu 1 with its sub-submenus
    sub1 = Composite("submenu1")
    sub11 = Child("sub_submenu 11")
    sub12 = Child("sub_submenu 12")
    sub1.append_child(sub11)
    sub1.append_child(sub12)

    # Submenu 2
    sub2 = Child("submenu2")

    # Top menu
    top = Composite("top_menu")
    top.append_child(sub1)
    top.append_child(sub2)
    top.component_function()
    # top_menu
    # submenu1
    # sub_submenu
    # 11
    # sub_submenu
    # 12
    # submenu2


if __name__ == "__main__":
    main()
