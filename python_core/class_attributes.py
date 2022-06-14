class Goal:
    text = "text"
    date = "data"
    complete = False

    def set_complete_true(self):
        self.complete = True


if __name__ == '__main__':
    a = Goal()
    a.set_complete_true()
    print(a.complete)  # should be true now, only for object a, because we use instance attribute

    a2 = Goal()
    print(a2.complete)
