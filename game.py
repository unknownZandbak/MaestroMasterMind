import random
import maestro as ma

"""
your comments need to be english, bring consistency to your variable names all englis or dutch
and sometimes a little to much information given in the comments for my taste.
the code is well written as far as i can see keep it up :]
"""


def gen_code():
    for i in range(0, 4):
        code[i] = random.randint(1, 6)


def make_guess():
    global round
    round += 1
    print(f"\nGok: {round}")
    guesses[round] = ma.gok(round, answers[round-1], guesses[round-1])


def gen_feedback():
    tmp_code = code.copy()
    tmp_guess = list(guesses[round]).copy()
    number = 0
    for i in guesses[round]:
        if tmp_code[number] == i:
            answers[round][0] += 1
            tmp_code[number] = 0
            tmp_guess[number] = 0
        number += 1
    number = 0
    for i in tmp_guess:
        if i in tmp_code and i != 0:
            answers[round][1] += 1
            tmp_code[tmp_code.index(i)] = 0
            tmp_guess[number] = 0
        number += 1
    # answers[round][1] -= answers[round][0]


# While True loop is used as a main game loop
while True:
    '''
    Instellen van een aantal variabellen zoals de code en gok zodat ze door elke functie gewijzigd kunnen worden
    Voor de kleuren gebruik ik getallen van 1 t/m 6 (zes verschillende "kleuren")
    Dit zorgt ervoor dat er met elke nieuwe game er een schoon blad is voor de nieuwe game
    '''
    code = ["%ph%", "%ph%", "%ph%", "%ph%"]
    guesses = [["%ph%", "%ph%", "%ph%", "%ph%"] for i in range(9)]
    answers = [[0, 0] for i in range(9)]
    round = 0
    win = False
    colorCode = {
        1: "Rood",
        2: "Blauw",
        3: "Groen",
        4: "Geel",
        5: "Zwart",
        6: "Oranje"
    }

    gen_code()
    print(f"\nCode gegenereerd: {code}")

    while round < 8:

        make_guess()
        print(f"De secret code is:      {code}")
        print(f"Gok gegenereerd:        {guesses[round]}")

        # a temp code var in order to correctly create feedback

        '''
        Voor feedback gebruik ik de volgende getallen met de bij genoteerde betekenis
        0: Fout
        1: Goede kleur maar niet op de juiste plek
        2: Goede kleur en op de juiste plek
        De positie van de getallen in het antwoord zeggen niet over welke "kleur" goed is en welke fout
        '''
        gen_feedback()
        print(f"Feedback gegenereerd:   {answers[round]}")

        # Check of de code goed geraden is
        if guesses[round] == code:
            win = True
            break
    if win:
        print(f"\n\nGefeliciteerd je hebt gewonnen in round {round} !!!!!\n")
        break
    else:
        print(f"\n\nHelaas je hebt de code niet goed geraden\n")
        break

    # if input("Wil je nog een keer spelen? j of n : ") == "j":
    #     continue
    # else:
    #     break
