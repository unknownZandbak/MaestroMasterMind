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


if __name__ == "__main__":
    op1()