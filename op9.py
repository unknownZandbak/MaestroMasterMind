import random
ch = random.randint(1, 255)
n = random.randint(-8, 8)


def schuiver():
    bitwaarde = bin(ch)[2:]
    byte = str(bitwaarde).zfill(8)
    if n > 8 or n < -8:
        print("Out of range")
    elif n > 0:
        tmp = byte[-n:]
        rest = byte[:-n]
        new_byte = tmp + rest
        return new_byte
    elif n < 0:
        tmp = byte[:-n]
        rest = byte[-n:]
        new_byte = rest + tmp
        return new_byte


print(schuiver())
