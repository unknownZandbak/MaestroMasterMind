def op1():
    aantal = int(input("Hoe Groot? : "))
    for i in range(0, aantal):
        print(i*"*")
    for x in range(aantal, 0, -1):
        print(x*"*")


def op1v2():
    aantal = int(input("Hoe Groot? : "))
    count = 0
    while count <= aantal:
        count += 1
        print(count*"*")
    while count > 1:
        count -= 1
        print(count*"*")


def op1v3():
    aantal = int(input("Hoe Groot? : "))
    for i in range(aantal, 1, -1):
        print(i*"*")
    for x in range(1, aantal+1):
        print(x*"*")


def op2():
    pass


def op3():
    pass


def op4():
    woord = "lepel"
    print(woord == woord[::-1])


def op5():
    pass


def op6():
    pass


def op7():
    pass


def op8():
    pass


def op9():
    pass


def op10():
    pass


def op11():
    pass


if __name__ == "__main__":
    op4()
