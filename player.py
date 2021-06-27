class Player:

    def __init__(self, isHuman: bool):
        self.isHuman = isHuman

    # print(len(set("eansj") & set("jeans")))

    def numShared(word1, word2):
        # print(len(set("beans") & set("jeans")))
        return len(set(word1) & set(word2))


    def isValid(word, dictionary, history):
        if len(word) != 5:
            return False

        for i in history:
            if len(set(i[0]) & set(word)) != i[1]:
                return False

        return word in dictionary


    def getValidWords(dictionary, history):
        valid = []

        for w in dictionary:
            cont = True
            for hh in history:
                if Player.numShared(w, hh[0]) != hh[1]:
                    cont = False
            
            if cont:
                valid.append(w)
        
        return valid


    def getHumanGuess(self, dictionary, history):
        guess = ""

        while not Player.isValid(guess, dictionary, history):
            guess = input("Guess a word: ")

            if not Player.isValid(guess, dictionary, history):
                print("Not a valid word.")

        return guess


    def heuristic(word, validWords, history):
        counts = [0, 0, 0, 0, 0, 0]

        for x in validWords:
            counts[Player.numShared(word, x)] += 1
        
        sum = 0;
        
        mean = (counts[0] + counts[1] + counts[2]) / 3.0
        
        
        sum += (mean - counts[0]) * (mean - counts[0])
        sum += (mean - counts[1]) * (mean - counts[1])
        sum += (mean - counts[2]) * (mean - counts[2])
        
        sum = 10000000 / (sum + 1)
        
        # temp = sum
        
        sum += 100 / (counts[3] + 1)
        sum += counts[4]
        
        
        limit4 = 10 - len(history)
        if limit4 < 2:
            limit4 = 2
        
        if counts[4] >= limit4:
            return -1 * counts[4];
        
        return sum;


    def getAIGuess(self, dictionary, history):
        valids = Player.getValidWords(dictionary, history)
        topVal = Player.heuristic(valids[0], valids, history)
        topWord = valids[0]

        for x in valids:
            currVal = Player.heuristic(x, valids, history)

            if currVal > topVal:
                topVal = currVal
                topWord = x

        return topWord

    
    def getGuess(self, dictionary, history):
        if self.isHuman:
            return self.getHumanGuess(dictionary, history)
        else:
            return self.getAIGuess(dictionary, history)
    

