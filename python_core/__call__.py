class Event(list):
    def __call__(self, *args, **kwargs):
        print("Event created...")


if __name__ == "__main__":
    e = Event()
    e()
