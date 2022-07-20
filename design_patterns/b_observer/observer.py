"""
Observer Pattern - one subject monitored by many observers.
One-to-many relationship between objects such as if one object is modified, its dependent objects are to be notified automatically.

Example: Elon-Musk profile in Twitter is Subject, his 65M followers are observers.

Problem:
- Subject to be monitored
- Observers to be notified

Scenario:
- Core temperature - reactors at a power plant.

Solution:
- Subject - abstract classes
    Attach
    Detach
    Notify
- Concrete subjects(Subject)

+ You haven’t to change the publisher’s code to add subscribers’ classes.
- Subscribers get notifications in random order.

Singleton related to Observer
"""


class Subject(object):  # Represents what is being 'observed'

    def __init__(self):
        self._observers = []  # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:  # If the observer is not already in the observers list
            self._observers.append(observer)  # append the observer to the list

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all the observers in the list
            if modifier != observer:  # Don't notify the observer who is actually updating the temperature
                observer.update(self)  # Alert the observers!


class Core(Subject):  # Inherits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()  # Notify the observers whenever somebody changes the core temperature


class TempViewer:
    def update(self, subject):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


if __name__ == "__main__":
    # Let's create our subjects
    c1 = Core("Core 1")

    # Let's create our observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Let's attach our observers to the first core
    c1.attach(v1)
    c1.attach(v2)

    # Let's change the temperature of our first core
    c1.temp = 80
    c1.temp = 90
