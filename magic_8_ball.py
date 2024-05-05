import random

question = input('What is your question? ')

outcomes = {1:'definitely', 2:'It is decidedly so', 3:'Without a doubt', 4:'Reply hazy, try again', 5: 'Ask again later.', 6:'Better not tell you now', 7: 'My sources say no.', 8: 'Outlook not so good.', 9: 'Outlook not so good.', 10: 'Very doubtful.'}

Magic_8_Ball = random.randint(0,10)

output = outcomes.get(Magic_8_Ball, 'Null')

print('Magic 8 Ball says: ', output)