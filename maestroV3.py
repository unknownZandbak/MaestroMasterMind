import random
import itertools
'''
Het volgende algoritme zijn gemaakt op basis van startegien die besrproken worden
in een paper van de universiteit van Groningen https://theses.liacs.nl/pdf/2018-2019-GraafSde.pdf.
In dit geval zal ik gebruik maken van de MiniMax Only Knuth Codes Algorithm
'''

# allemogelijke opties genereren
possible_guesses = list(itertools.product(range(1, 7), repeat=4))


def gok(round, answer, guess):
    # Hard code de eerste gok naar AABB
    if round == 1:
        return [1, 1, 2, 2]
    elif round == 2:
        bereken_nieuwe_opties(answer, guess)
        return [3, 4, 5, 5]
    # elif round == 3:
    #     bereken_nieuwe_opties(answer, guess)
    #     return [4, 4, 6, 6]
    else:
        bereken_nieuwe_opties(answer, guess)
        nieuwe_opties = minmax()
        return nieuwe_opties[0]


def bereken_nieuwe_opties(answer, guess):
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


def gen_feedback(guess, code):
    answer = [0, 0]
    # a temp code en guess varriable is created in order to correctly create feedback
    tmp_code = list(code).copy()
    tmp_guess = list(guess).copy()
    number = 0
    for i in guess:
        if tmp_code[number] == i:
            answer[0] += 1
            tmp_code[number] = 0
            tmp_guess[number] = 0
        number += 1
    number = 0
    for i in tmp_guess:
        if i in tmp_code and i != 0:
            answer[1] += 1
            tmp_code[tmp_code.index(i)] = 0
            tmp_guess[number] = 0
        number += 1
    return answer


def minmax():
    all_answers = []
    newnew = []
    tmplist = []
    times_found = {}
    scores = {}
    all_codes = list(itertools.product(range(1, 7), repeat=4))
    for i in possible_guesses:
        for j in possible_guesses:
            feedback = gen_feedback(i, j)
            all_answers.append(feedback)

        for i in all_answers:
            tmplist.append(str(i))
        unique_answers = set(tmplist)

        for x in unique_answers:
            times_found.update({x: all_answers.count(x)})

        highest = max(times_found.values())
        scores.update({str(i): highest})

    lowest = min(times_found.values())

    for i in possible_guesses:
        if scores.get(str(i)) == lowest:
            newnew.append(i)
    return possible_guesses
