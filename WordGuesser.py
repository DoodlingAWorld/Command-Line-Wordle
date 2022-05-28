from dbm.ndbm import library
from random import random as rn

##
# WordGuesses
#
# This class contains the fields and methods that will support playing the game.
#
# @author ArchitVarun
#
# @version 1.1, (2022-05-22)
##

class WordGuesser:
    rows, cols = (5, 5)
    playingField = [["" for i in range(5)] for j in range(rows)]
    solution = ""
    round = 0

    def __init__(self, input_solution):
        self.solution = input_solution
        self.round = 1
    
    def getRound(self):
        return self.round
    
    def getSolution(self):
        return self.solution
    
    def setPlayingField(self, inputPlayingField):
        self.playingField = inputPlayingField
    
    def setRound(self, inputRound):
        self.round = inputRound
    
    def checkGuess(self, inputGuess):
        status = False
        solutionArray = list(self.solution)
        guessArray = list(inputGuess)

        if inputGuess == self.solution:
            status = True
            for i in range(len(guessArray)):
                self.playingField[self.round - 1][i] = "'" + guessArray[i] + "'"
        else:
            status = False
            for i in range(len(self.playingField[self.round - 1])):
                for j in range(len(guessArray)):
                    if guessArray[j] == solutionArray[j]:
                        self.playingField[self.round - 1][j] = "'" + guessArray[j] + "'"
                    elif guessArray[j] in self.solution:
                        self.playingField[self.round - 1][j] = "*" + guessArray[j] + "*"
                    else:
                        self.playingField[self.round - 1][j] = "{" + guessArray[j] + "}"
        
        return status
    
    def printField(self):
        for i in range(len(self.playingField)):
            for j in range(len(self.playingField[i])):
                if j == len(self.playingField[i]):
                    print(self.playingField[i][j])
                else:
                    print(self.playingField[i][j] + " | ", end="")
            print("\n")
    


    

        
