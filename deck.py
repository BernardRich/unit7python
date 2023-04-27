import random

def shuffled_deck():
    basic_deck = list(range(2,15))*4
    
    random.shuffle(basic_deck)
    
    return basic_deck

print(shuffled_deck())

