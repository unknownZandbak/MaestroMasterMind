import random

# Instellen van een aantal variabellen zoals de code en gok zodat ze door elke functie gewijzigd kunnen worden
# Voor de kleuren gebruik ik getallen van 1 t/m 6 (zes verschillende "kleuren")

code = [0, 0, 0, 0]
gok = [1, 1, 1, 1]
answer = [0, 0, 0, 0]
cnt = 1


def startup():
    code[0] = random.randint(1, 6)
    code[1] = random.randint(1, 6)
    code[2] = random.randint(1, 6)
    code[3] = random.randint(1, 6)
    print(f"\nCode gegenereerd: {code}")


def question():
    global cnt
    print(f"\nGok {cnt}")
    gok[0] = random.randint(1, 6)
    gok[1] = random.randint(1, 6)
    gok[2] = random.randint(1, 6)
    gok[3] = random.randint(1, 6)
    cnt += 1
    print(f"Gok gegenereerd {gok}")

# Voor feedback gebruik ik d volgende getallen met de bij genoteerde betekenis
# 0: Fout
# 1: Goede kleur maar niet op de juiste plek
# 2: Goede kleur en op de juiste plek
# De positie van de getallen in het antwoord zeggen niet over welke "kleur" goed is en welke fout


def feedback():
    for i in range(0, 3):
        if gok[i] == code[i]:
            answer[i] = 2
        elif gok[i] in code:
            answer[i] = 1
        else:
            answer[i] = 0
    print(f"Feedback gegenereerd: {answer}")


startup()
question()
feedback()
