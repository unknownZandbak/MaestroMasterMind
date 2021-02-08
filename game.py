import random
import maestro as ma


# While True loop is used as a main game loop
while True:

    # Instellen van een aantal variabellen zoals de code en gok zodat ze door elke functie gewijzigd kunnen worden
    # Voor de kleuren gebruik ik getallen van 1 t/m 6 (zes verschillende "kleuren")
    # Dit zorgt ervoor dat er met elke nieuwe game er een schoon blad is voor de nieuwe game
    code = ["%ph%", "%ph%", "%ph%", "%ph%"]
    gokken = [["%ph%", "%ph%", "%ph%", "%ph%"] for i in range(9)]
    answer = ["%ph%", "%ph%", "%ph%", "%ph%"]
    answers = [answer for i in range(9)]
    ronde = 0
    win = False
    colorCode = {
        1: "Rood",
        2: "Blauw",
        3: "Groen",
        4: "Geel",
        5: "Zwart",
        6: "Oranje"
    }
    # Het maken van de code door random een getal tussen 1 t/m 6 te kiezen voor ellke index
    for i in range(0, 4):
        code[i] = random.randint(1, 6)
    print(f"\nCode gegenereerd: {code}")

    while ronde < 8:

        # Hier doen we nu een random gok voordat we het algoritme gaan implementeren
        ronde += 1
        print(f"\nGok {ronde}")
        gokken[ronde] = ma.gok(ronde, answers, gokken)
        print(f"Gok gegenereerd {gokken[ronde]}")

        # een tijdelijke lijst voor het maken van feedback
        tmp_code = [i for i in code]

        '''
        Voor feedback gebruik ik d volgende getallen met de bij genoteerde betekenis
        0: Fout
        1: Goede kleur maar niet op de juiste plek
        2: Goede kleur en op de juiste plek
        De positie van de getallen in het antwoord zeggen niet over welke "kleur" goed is en welke fout
        '''
        nummer = 0
        for i in gokken[ronde]:
            if i in tmp_code:
                if gokken[ronde].index(i) == code.index(i):
                    answers[ronde][nummer] = 2
                else:
                    answers[ronde][nummer] = 1
                tmp_code.remove(i)
            else:
                answers[ronde][nummer] = 0
            nummer += 1
        print(f"Feedback gegenereerd: {answer}")

        # Check of de code goed geraden is
        if gokken[ronde] == code:
            win = True
            break
    if win:
        print(f"\n\nGefeliciteerd je hebt gewonnen in ronde {ronde} !!!!!\n")
        break
    else:
        print(f"\n\nHelaas je hebt de code niet goed geraden\n")
        break
    # if input("Wil je nog een keer spelen? j of n : ") == "j":
    #     continue
    # else:
    #     break
