import random
import itertools
'''
Het volgende algoritme zijn gemaakt op basis van startegien die besrproken worden 
in een paper van de universiteit van Groningen https://canvas.hu.nl/courses/22629/files/1520303/download?wrap=1. 
In dit geval zal ik gebruik maken van de simple strategy
'''

# allemogelijke opties genereren
possible_guesses = list(itertools.product(range(1, 7), repeat=4))


def gok(round, answer, guess):
    # Hard code de eerste gok naar AABB
    if round == 1:
        return [1, 1, 2, 2]
    else:
        nieuwe_opties = bereken_nieuwe_opties(round, answer, guess)

        return random.choice(nieuwe_opties)


def bereken_nieuwe_opties(round, answer, guess):
    tmp_answer = [0, 0, 0, 0]

    for tmp_code in possible_guesses:
        number = 0
        for i in tmp_code:
            if i == guess[number]:
                tmp_answer[number] = 2
                list(tmp_code)[number] = 0
            number += 1
        number = 0
        for i in tmp_code:
            if i in guess:
                tmp_answer[number] = 1
            number += 1
        if tmp_answer != answer:
            possible_guesses.remove(tmp_code)
    return possible_guesses
