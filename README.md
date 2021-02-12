# MaestroMasterMind
In this project i have i have recreated 2 algorithms in order to solve a game of mastermind.
The algorithms a saved is seperate files and imported to the main file `game.py`.
***
### MaestroV1

`maestro.py` is based on the simple strategy mentiond in a paper from the university of groningen titled:**YET ANOTHER MASTERMIND STRATEGY**.
The strategy is written as follows:

##### 2.1 A Simple Strategy
###### The first strategy by Shapiro (Shapiro, 1983) (it is also published in (Sterling and Shapiro, 1994)). His algorithm does is the following: the combinations are somehow ordered (usually alphabetically) and the first combination is asked. The answer is received. The next question is the first one in the ordering that is consistent with the answers given so far. And so on until the combination is cracked. A crucial drawback to this strategy, however, is that it looks at the informativity of questions very marginally. One can only be certain that one does not know the answer already, but that is all.
---
### MaestroV2

`maestrV2.py` is based on the  "MiniMax Only Knuth Codes Algorithm" which is based on th worst case strategy/ five guess algorithm, these strategy's are mentioned in a paper of the university of leiden titled:**Cracking the Mastermind Code** written by Sylvester de Graaf.
Source: https://theses.liacs.nl/pdf/2018-2019-GraafSde.pdf.

---
### MaestroV3

`maestroV3.py` is the same as `maestrov2.py` but i hard coded the first 2 guesses to make it a lot faster to run, because it can elimenate more options before it loops through the list making it alot faster.

***
## Pseudo Code

#### MaestroV1
possible_guesses = list(itertools.product(range(1, 7), repeat=4))


def gok(round, answer, guess):
    if round == 1:
        return [1, 1, 2, 2]
    else:
        nieuwe_opties = bereken_nieuwe_opties(answer, guess)
        return eerste item uit nieuwe opties


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
    return possible_guesses