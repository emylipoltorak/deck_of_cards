from card import Card
import random
from operator import attrgetter

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck:
    def __init__(self):
        self.cards = self.build_deck()

    def build_deck(self):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        return deck

    def shuffle(self):
        return random.shuffle(self.cards)

    def cut(self):
        cut_int = random.randint(20, 30)
        self.cards = self.cards[cut_int:]+self.cards[:cut_int]
        return self.cards

    def draw(self):
        return self.cards.pop(0)

    def sort(self):
        self.cards = sorted(self.cards, key = attrgetter('value', 'suit_value'))
        return self.cards

if __name__ == '__main__':
    new_deck = Deck()
    new_deck.shuffle()
    new_deck.cut()
    new_deck.sort()
    print(new_deck.cards)
