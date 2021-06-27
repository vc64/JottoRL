from mastermind import Mastermind
from player import Player

class Jotto:

    def getDictionary():
        file = open("C:/Users/viche/Desktop/vc/code/JottoPy/raw_words.txt", "r")
        words = file.readlines()
        return [n[:-1] for n in words]
            
        
    def playGame():
        dictionary = Jotto.getDictionary()
        history = []
        mind = Mastermind(dictionary)

        isHuman = input("Human player (1) or computer player (2)?")

        player = Player(isHuman == "1")

        clue = 0
        while clue != 5:
            guess = player.getGuess(dictionary, history)
            clue = mind.getClue(guess)
            history.append((guess, clue))
            print(guess.upper() + " " + str(clue))
    