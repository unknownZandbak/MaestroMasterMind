import itertools
'''
Het volgende algoritme zijn gemaakt op basis van startegien die besrproken worden 
in een paper van de universiteit van Groningen https://canvas.hu.nl/courses/22629/files/1520303/download?wrap=1. 
In dit geval zal ik gebruik maken van de worst case strategy
'''

# allemogelijke opties genereren
possible_guesses = list(itertools.product(range(1, 7), repeat=4))


def gok(ronde, answers, gokken):
    # Hard code de eerste gok naar AABB
    if ronde == 1:
        return [1, 1, 2, 2]
    else:
        analyse(ronde, answers, gokken)


def analyse(ronde, answers, gokken):
    nummer = 0
    for i in gokken[ronde]:
        tmp_code = [i for i in possible_guesses]
        tmp_answer = ["%ph%", "%ph%", "%ph%", "%ph%"]
        if i in tmp_code:
            if gokken[ronde].index(i) == possible_guesses.index(i):
                answers[ronde][nummer] = 2
            else:
                answers[ronde][nummer] = 1
            tmp_code.remove(i)
        else:
            answers[ronde][nummer] = 0
        nummer += 1
