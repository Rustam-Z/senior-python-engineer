class PrintNumber:
    def __init__(self, max):
        self.num = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num


if __name__ == '__main__':
    print_num = PrintNumber(3)
    print_num_iter = iter(print_num)

    print(next(print_num_iter))  # 1
    print(next(print_num_iter))  # 2
    print(next(print_num_iter))  # 3
    print(next(print_num_iter))  # raises StopIteration
