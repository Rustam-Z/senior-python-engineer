def f(x):
    print("outer", x)
    if x == 1:
        print("inside if", x)
        return x
    else:
        x -= 1
        print("inner", x)
        f(x)

    print("Khushnura")
    return "Rustam"


if __name__ == '__main__':
    x = 2
    print(f(x), x)
