# MaestroMasterMind
In this project i have i have recreated 2 algorithms in order to solve a game of mastermind.
The algorithms a saved is seperate files and imported to the main file `game.py`.

`maestro.py` is based on the simple strategy mentiond in a paper from the university of groningen titled:**YET ANOTHER MASTERMIND STRATEGY**.
The strategy is written as follows:

##### 2.1 A Simple Strategy
###### The first strategy by Shapiro (Shapiro, 1983) (it is also published in (Sterling and Shapiro, 1994)). His algorithm does is the following: the combinations are somehow ordered (usually alphabetically) and the first combination is asked. The answer is received. The next question is the first one in the ordering that is consistent with the answers given so far. And so on until the combination is cracked. A crucial drawback to this strategy, however, is that it looks at the informativity of questions very marginally. One can only be certain that one does not know the answer already, but that is all.
***
`maestrV2.py` is based on the  "MiniMax Only Knuth Codes Algorithm" which is based on th worst case strategy/ five guess algorithm, these strategy's are mentioned in a paper of the university of leiden titled:**Cracking the Mastermind Code** written by Sylvester de Graaf.
Source: https://theses.liacs.nl/pdf/2018-2019-GraafSde.pdf.
***
`maestroV3.py` is the same as `maestrov2.py` but i hard coded the first f
