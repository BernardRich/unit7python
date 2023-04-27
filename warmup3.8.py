import random

card_value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

suits = ['Spades','Clubs','Diamonds','Hearts']

def pick5card():
    count = 0
    while count<5:
        randomvalue = card_value [random.randint(0,12)]
        randomsuit = suits[random.randint(0,3)]
        print('you\'ve Drawn A ' + randomvalue + ' of ' + randomsuit)
        count+=1

pick5card()                   