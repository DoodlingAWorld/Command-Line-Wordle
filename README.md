# Command-Line-Wordle

This program is a basic command line interface of the popular game Wordle. I had previously created this project for a CS Course I took in Java. I converted the program into Python, which is what you see here.

## WordLibrary.py
Very basic Python class that consists of three methods:
 a) A constructor
 b) cleanLibrary: This method goes through the user provided list and removes any word longer than 5 letters.
 c) chooseWord: This method selects, at random, a word from the user provided list that will be the solution

## WordGuesser.py
This Python class contains main guessing methods. I won't go into detail, but the main methods are checkGuess and printField. checkGuess compares the user's guess with the program's solution. printField, as its name suggests, prints the playing board in a formatter manner.

## WordGame.py
This is the main python file for the project. It contains the logic of the code, and allows users to exit from the program at any point of time. Logic is currently sequential, but I will attempt to make it concurrent in the future.

