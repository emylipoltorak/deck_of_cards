class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()
        self.suit_value = ['Spades', 'Hearts', 'Clubs', 'Diamonds'].index(self.suit)

    def get_value(self):
        royalty = ['J', 'K', 'Q', 'A']
        try:
            return int(self.rank)
        except ValueError:
            if self.rank in royalty:
                return 11 + royalty.index(self.rank)

    def __repr__(self):
        royalty = {'A': 'Ace', 'K': 'King', 'Q': 'Queen', 'J': 'Jack'}
        try:
            return '{} of {}'.format(royalty[self.rank], self.suit)
        except KeyError:
            return '{} of {}'.format(self.rank, self.suit)
