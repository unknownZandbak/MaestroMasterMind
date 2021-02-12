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

```
possible_guesses = all possible guesses (only generated once)

def guess(round, previouse feedback, guess):
    if round == 1:
        return [1, 1, 2, 2]
    else:
        nieuwe_opties = bereken_nieuwe_opties(previouse feedback, guess)
        return eerste item uit nieuwe opties


def bereken_nieuwe_opties(previouse feedback, guess):
    tmp_viouse feedback = [0, 0]
    copy_possible_guesses = possible_guesses.copy()

    for code in copy_possible_guesses:
        tmp_feedback[0] = 0
        tmp_feedback[1] = 0
        tmp_code = copy of code
        tmp_guess = copy of guess
        number = 0
        for i in guess:
            if tmp_code[number] == i:
                tmp_feedback[0] += 1
                change the number in tmp_code to 0
                change the number in tmp_guess to 0
            number + 1
        number = 0
        for i in tmp_guess:
            if i is in tmp_code and is not a 0:
                change the number in tmp_code to 0
                change the number in tmp_guess to 0
            number += 1
        if tmp_feedback is not the same as previouse feedback:
            remove code from possible_guesses
    return possible_guesses
```
---
#### MaestroV2

```
def minmax():
    for i in possible_guesses:
        for j in possible_guesses:
            feedback = gen_feedback(i, j)
            times_found[feedback]++

        highest = get the highest times found feedback
        scores[i] = highest

    lowest = get the lowest times found feedback

    for i in possible_guesses:
        if scores[] is the same as lowest:
            add code to new_posibble_guesses
    return new_possible_guesses

```
---
#### Maestrov3 
the only change opposte to maestroV2 is in de geuss function
```
possible_guesses = all possible guesses (only generated once)

def guess(round, previouse feedback, guess):
    if round == 1:
        return [1, 1, 2, 2]
    elif round == 2:
        bereken_nieuwe_opties(previouse feedback, guess)
        return [4, 4, 5, 5]
    else:
        bereken_nieuwe_opties(previouse feedback, guess)
        nieuwe_opties = minmax()
        return eerste item uit nieuwe opties
```