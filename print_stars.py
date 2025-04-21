def printStars(n):
    for i in range(n):
        print("*" * (i + 1))

printStars(5)


def printStarsReverse(n):
    for i in range(n, 0, -1):
        print("*" * i)

printStarsReverse(5)
