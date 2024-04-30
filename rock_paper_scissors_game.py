from random import randint
   
class RockPaperScissors:
    def __init__(self):
        self.option = ''
        self.randomPlayer = ''
        self.result = ''

    def setOption(self, option):
        options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        self.option = options.get(option, 'Null')
    
    def setOthersOption(self):
        options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        randomOption = randint(1, 3)
        self.randomPlayer = options.get(randomOption, 'Null')
        
    def setScore(self):
        outcomes = {
            ('Rock', 'Rock'): 'Its a Tie :|',
            ('Rock', 'Paper'): 'The bot won :(',
            ('Rock', 'Scissors'): 'You won :)',
            ('Paper','Paper'): 'Its a Tie :|',
            ('Paper', 'Scissors'): 'The bot won :(',
            ('Paper', 'Rock'): 'You won :)',
            ('Scissors', 'Rock'): 'The bot won :(',
            ('Scissors', 'Paper'): 'You won :)',
            ('Scissors', 'Scissors'): 'Its a tie :|'        
            }
        self.result = outcomes.get((self.option, self.randomPlayer), 'Invalid')
        
    def __str__(self):
        return 'You have chosen: {0}\nYour opponent has chosen: {1}\n\n{2}'.format(self.option, self.randomPlayer, self.result)
          
test = RockPaperScissors()
test.setOption(1)
test.setOthersOption()
test.setScore()
print(test)


