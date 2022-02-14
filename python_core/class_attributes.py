class Goal():
    text = "text"
    date = "data"
    complete = False

    def set_complete_true(self):
        self.complete = True


a = Goal()
a.set_complete_true()
print(a.complete)  # should be true now, only for object a

a2 = Goal()
print(a2.complete)

