import random

target = random.randint(0, 10)
shot = int(input("Gok het getal tussen 0 en 10 : "))
while target != shot:
    shot = int(input("\nTry again : "))
print("\nHet is je gelukt!!!!!!!!!!!!!!!")
