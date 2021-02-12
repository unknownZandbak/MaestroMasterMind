import random
import maestro as ma
import maestroV2 as maV2
import maestroV3 as maV3


def gen_code():
    for i in range(0, 4):
        code[i] = random.randint(1, 6)


def make_guess():
    print(f"\nGok: {round}")
    if gamemode_choice == 1:
        guesses[round] = ma.gok(round, answers[round-1], guesses[round-1])
    elif gamemode_choice == 2:
        guesses[round] = maV2.gok(round, answers[round-1], guesses[round-1])
    elif gamemode_choice == 3:
        guesses[round] = maV3.gok(round, answers[round-1], guesses[round-1])


def gen_feedback():
    # a temp code en guess varriable is created in order to correctly create feedback
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
    gamemode_choice = int(input(
        "Kies een algorithme om te laten spelen.\n1: Simple strategy\n2: MiniMax Only Knuth Codes\n3: MiniMax Only Knuth Codes + mijn eigen heuristiek\nKeuze: "))
    if gamemode_choice != 1 or gamemode_choice != 2 or gamemode_choice != 3:
        print("\nVerkeerde optie ingevoerd\nProgramma stopt nu")
        break
    gen_code()
    print(f"\nSecret code gegenereerd: {code}")

    while round < 8:

        round += 1
        make_guess()
        print(f"De secret code is:      {code}")
        print(f"Gok gegenereerd:        {guesses[round]}")

        gen_feedback()
        print(f"Feedback gegenereerd:   {answers[round]}")

        # Check of de code goed geraden is
        if answers[round] == [4, 0]:
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
