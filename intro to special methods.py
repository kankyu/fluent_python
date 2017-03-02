import collections

Card = collections.namedtuple('Card', ['card', 'suit'])

class Deck:

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = Deck()

for card in deck:
    print(card)


print(len(deck))

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)


# sorting
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
