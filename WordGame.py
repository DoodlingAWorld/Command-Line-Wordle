from dbm.ndbm import library
from random import random as rn
from re import U
import WordGuesser as wg
import WordLibrary as wl

##
# WordGame
#
# This class contains the main method and menu interface that lets the user play the game.
#
# @author ArchitVarun
#
# @version 1.1, (2022-05-22)
##

class WordGame:
    welcome = "Ready to play?"
    yesNo = "1.Yes\n2.No"
    noPlay = "Maybe next time!"
    currentRoundLabel = "Current Round: {}"
    enterGuess = "Please enter a guess!"
    winner = "You got the answer!"
    outOfGuesses = "You ran out of guesses!"
    solutionLabel = "Solution: "
    incorrect = "That's not it!"
    keepPlaying = "Would you like to make another guess?"
    enterWords = "Please enter a comma-separated list of words"

    userChoice = 1
    choiceCheck = False
    userGuess = ""
    counter = 1


    rows, cols = (5, 5)
    defaultPlayingField = [["" for i in range(5)] for j in range(rows)]

    userWords = list(input(enterWords + ": ").split(","))
    accessWl = wl.WordLibrary(userWords)
    accessWG = wg.WordGuesser(accessWl.chooseWord())


    while userChoice == 1:
        print(welcome)
        userChoice = int(input(yesNo + "\n"))

        while userChoice != 2:
            print(currentRoundLabel.format(accessWG.getRound()))
            accessWG.printField

            userGuess = input(enterGuess + "\n")
            accessWG.checkGuess(userGuess)
            counter += 1

            if accessWG.checkGuess(userGuess) == True:
                print(winner)
                accessWG.printField()
                counter = 1
                accessWG = wg.WordGuesser(accessWl.chooseWord())
                accessWG.setRound(counter)
                accessWG.setPlayingField(defaultPlayingField)
                break

            if accessWG.checkGuess(userGuess) == False:
                accessWG.setRound(counter)
                if counter > 5:
                    print(outOfGuesses)
                    print(solutionLabel + accessWG.getSolution())
                    accessWG.printField()
                    break
                elif counter <= 5:
                    accessWG.printField()
                    print(incorrect)
                    print(keepPlaying)
                    userChoice = int(input(yesNo + "\n"))
                
                    if counter < 5 and userChoice == 2:
                        accessWG.printField()

                        print(welcome)
                        userChoice = int(input(yesNo + "\n"))
                        
                        if userChoice == 1:
                            counter = 1
                            accessWG = wg.WordGuesser(accessWl.chooseWord())
                            accessWG.setRound(counter)
                            accessWG.setPlayingField(defaultPlayingField)
                            continue
                        elif userChoice == 2:
                            break
    print(noPlay)
            





