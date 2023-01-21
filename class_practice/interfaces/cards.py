import collections
from random import shuffle


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self) -> str:
        card_list = ''
        for i in self._cards:
            card_list = card_list + str(i.rank) + ' ' + str(i.suit) + '\n'
        return card_list

    def __setitem__(self, position, card):
        self._cards[position] = card
        

if __name__ == '__main__':
    cards = FrenchDeck()
    print(cards)
    shuffle(cards)
    print('\n')
    print(cards)
    
