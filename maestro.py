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
        # return random.choice(nieuwe_opties)
        return nieuwe_opties[0]


def bereken_nieuwe_opties(round, answer, guess):
    tmp_answer = [0, 0]
    copy_possible_guesses = possible_guesses.copy()

    for code in copy_possible_guesses:
        tmp_answer[0] = 0
        tmp_answer[1] = 0
        tmp_code = list(code).copy()
        tmp_guess = list(guess).copy()
        number = 0
        for i in guess:
            if tmp_code[number] == i:
                tmp_answer[0] += 1
                x = list(tmp_code)
                x[number] = 0
                tmp_code = tuple(x)
                y = list(tmp_guess)
                y[number] = 0
                tmp_guess = tuple(y)

            number += 1
        number = 0
        for i in tmp_guess:
            if i in tmp_code and i != 0:
                tmp_answer[1] += 1
                x = list(tmp_code)
                x[x.index(i)] = 0
                tmp_code = tuple(x)
                y = list(tmp_guess)
                y[number] = 0
                tmp_guess = tuple(y)
            number += 1
        if tmp_answer != answer:
            possible_guesses.remove(code)
    return possible_guesses
