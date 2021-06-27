from random import randint
from player import Player

class Mastermind:

    hiddenWord = ""

    def __init__(self, dictionary):
        self.hiddenWord = dictionary[randint(0,len(dictionary)-1)]

    def setWord(word):
        self.hiddenWord = word

    def getWord(self):
        return self.hiddenWord

    def getClue(self, guess):
        if guess == "bonks":
            print(self.hiddenWord)
            print("e")
        return Player.numShared(self.getWord(), guess)