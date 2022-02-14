# concrete course
class DSA():
    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000
        return self.fee

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"


# concrete course
class SDE():
    """Class for Software development Engineer"""

    def Fee(self):
        self.fee = 10000
        return self.fee

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"


# concrete course
class STL():
    """class for Standard Template Library of C++"""

    def Fee(self):
        self.fee = 5000
        return self.fee

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"


# main method
if __name__ == "__main__":
    sde = SDE()  # object for SDE
    dsa = DSA()  # object for DSA
    stl = STL()  # object for STL

    print(f'Name of Course: {sde} and its Fee: {sde.Fee()}')
    print(f'Name of Course: {stl} and its Fee: {stl.Fee()}')
    print(f'Name of Course: {dsa} and its Fee: {dsa.Fee()}')
