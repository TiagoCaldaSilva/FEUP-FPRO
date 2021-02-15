import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]
haands = []


def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


def choose(items):
    """Choose and return a random item"""
    return random.choice(items)


def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


def card_value(card):
    if 49 <= ord(card[1]) <= 57 and len(card) != 3:
        value = int(card[1])
    elif card[1] == "A":
        value = 11
    else:
        value = 10
    if card[0] == "♠" or card[0] == "♣":
        return 2 * value
    return value


def play(seed):
    random.seed(seed)
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        handss = []
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            handss.append((name, card[0] + card[1]))
        haands.append(handss)
 
    #Verificar o vencedor:
    points = {"P1": 0, "P2": 0, "P3": 0, "P4": 0}
    result = []
    for _ in haands:
        round_winner = []
        t = 0
        for i in _:
            value = card_value(i[1])
            if value > t:
                round_winner = [i[0], ]
                t = value
            elif value >= t:
                round_winner.append(i[0])
        for z in round_winner:
            points[z] += 1
    for k, v in points.items():
        result.append((k, v))
    result = sorted(result, key=lambda x: (x[1]), reverse=True)
    r = ""
    print(result)
    for i, v in enumerate(result):
        r += v[0] + " "

        if v[1] == result[i + 1][1]:
            continue
        else:
            break
    return r.rstrip(" ")

print(play(123))