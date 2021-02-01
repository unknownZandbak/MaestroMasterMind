import random


def genlst(lengte):
    lst = [1]
    for i in range(2, lengte+1):
        lst.insert(random.randrange(0, i-1), i)
    # print(lst)
    return sorted(lst)


print(genlst(int(input("Hoelang moet de lijst zijn? : "))))
