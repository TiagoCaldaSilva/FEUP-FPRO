import random
Suits = ["♠","♡","♢","♣"]
Ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
Deck = [s + str(r) for s in Suits for r in Ranks]
random.shuffle(Deck)