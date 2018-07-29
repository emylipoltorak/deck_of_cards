import unittest
from card import Card
from deck import Deck

class TestCardProperties(unittest.TestCase):
    def setUp(self):
        self.ace_of_hearts = Card('Hearts', 'A')

    def test_card_value(self):
        self.assertEqual(self.ace_of_hearts.value, 14)

    def test_card_suit(self):
        self.assertEqual(self.ace_of_hearts.suit, 'Hearts')

    def test_card_rank(self):
        self.assertEqual(self.ace_of_hearts.rank, 'A')

    def test_card_suit_value(self):
        self.assertEqual(self.ace_of_hearts.suit_value, 1)

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_contains_only_cards(self):
        for c in self.deck.cards:
            self.assertIsInstance(c, Card)

    def test_initial_deck_order(self):
        self.assertEqual(self.deck.cards[0].suit, 'Spades')
        self.assertEqual(self.deck.cards[13].rank, '2')
        self.assertEqual(self.deck.cards[51].value, 14)

    def test_shuffle(self):
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards[0].value, 2)

    def test_cut(self):
        bottom_card = self.deck.cards[0]
        self.deck.cut()
        self.assertNotEqual(self.deck.cards[0], bottom_card)

    def test_sorted_deck_order(self):
        self.deck.sort()
        self.assertEqual(self.deck.cards[3].rank, '2')
        self.assertEqual(self.deck.cards[51].suit, 'Diamonds')

    def test_draw(self):
        self.assertIsInstance(self.deck.draw(), Card)
        self.assertEqual(len(self.deck.cards), 51)


if __name__ == '__main__':
    unittest.main()
