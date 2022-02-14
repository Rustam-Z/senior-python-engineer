class Event(list):
    def __call__(self, *args, **kwargs):
        print("Event created...")


e = Event()

e()
