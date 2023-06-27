import random


class NumberAlgo:
    currentNumber = 0
    triesDone = 0
    triesLimit = 100
    high = 100
    low = 0
    conditionToWin = {'Message': 'The number is correct!!!'}
    tooLow =  {'Message': 'The number is to low, please try again'}
    tooHigh =  {'Message': 'The number is to high, please try again'}
    winMessage = f"Win! ,Number of guesses: {triesDone}"
    LoseMessage = f"Lose! ,Number of guesses: {triesDone}"
    

    def __init__(self):
        pass


    def TriesDone(self):
        self.winMessage = f"Win! ,Number of guesses: {self.triesDone}"
        self.LoseMessage = f"Lose! ,Number of guesses: {self.triesDone}"


    def setNumber(self):
       self.currentNumber = int(self.high / 2)
       return

    def NumberAlgo(self,respone):
        self.triesDone += 1
        print(f"Number of Tries: {self.triesDone}")
        print(f"Current number: {self.currentNumber}")
        if(self.triesDone >= self.triesLimit):
            print(self.LoseMessage)
            return self.LoseMessage
        else:
            if(respone == self.conditionToWin):
                self.TriesDone()
                print(self.winMessage)
                return self.winMessage
            elif respone == self.tooLow:
                self.low = self.currentNumber
                self.currentNumber = random.randint(self.low, self.high)
                print(respone)
                return 
            elif respone == self.tooHigh:
                self.high = self.currentNumber
                self.currentNumber = random.randint(self.low, self.high)
                print(respone)
                return
      
    
