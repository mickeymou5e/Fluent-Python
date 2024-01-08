import collections
from random import choice
Card = collections.namedtuple("Card", ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for  n in range(2,11)]+list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7','Diamonds')

deck = FrenchDeck()

len(deck)

deck[0]

choice(deck)

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

Card('7',"hearts") in deck

