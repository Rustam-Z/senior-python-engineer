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


class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        """Interface method"""
        pass


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        # Component.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)  # using super()

        # This is where we store the name of the composite object
        self.name = args[0]  # First argument is the "name"

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print("{}".format(self.name))
        print(self.children)  # Just for debuggint purposes

        # Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


# Build a top-level composite menu
top = Composite("top_menu")

# Build a composite submenu 1
sub1 = Composite("submenu1")

sub11 = Child("sub_submenu 11")  # Create a new child sub_submenu 11
sub12 = Child("sub_submenu 12")  # Create a new Child sub_submenu 12

sub1.append_child(sub11)  # Add the sub_submenu 11 to submenu 1
sub1.append_child(sub12)  # Add the sub_submenu 12 to submenu 1

# Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

# Let's test if our Composite pattern works!
top.component_function()
