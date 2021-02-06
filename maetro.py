import random
# mogelijke nummers voor de code
# elke kleur mag maximaal 2 keer gebruikt worden
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# nummers staat gelijk aan een kleur
color_binds = {
    1: "Rood",
    2: "Blauw",
    3: "Groen",
    4: "Geel",
    5: "Zwart",
    6: "Oranje"
}

secret_code = random.choices(numbers, k=4)
print(secret_code)
