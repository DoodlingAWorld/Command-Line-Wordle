from dbm.ndbm import library
import random

##
# WordLibrary
#
# This class contains the library of words used in the puzzle.
#
# @author ArchitVarun
#
# @version 1.1, (2022-05-22)
##

class WordLibrary:
    library = [] # Declaring an empty list for the words provided by the user

    def __init__(self, input_library):
        self.library = input_library
        self.clean_library()
    
    def clean_library(self):
        count = 0 # variable to count number of words not equal to 0
        for word in self.library:
            if len(word) != 5:
                self.library.remove(word)
    
    def chooseWord(self):
        chosenWord = random.choice(self.library)
        return chosenWord
    

    
    



