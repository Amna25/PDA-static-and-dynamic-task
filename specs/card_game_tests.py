import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):

        self.card = Card('clubs', 5)
        self.cardgame = CardGame()

    def test_can_check_ace_True(self):
        card = Card("spades", 1)
        self.assertEqual(True, self.cardgame.check_for_ace(card))

    def test_can_check_ace_False(self):
        card = Card("Hearts", 5)
        self.assertEqual(False, self.cardgame.check_for_ace(card))

    def test_can_check_heighest_card(self):
        card1 = Card('heart', 7)
        card2 = Card('diamond', 1)
        self.assertEqual(card1, self.cardgame.highest_card(card1, card2))

    def test_can_count_total_cards(self):
        card1 = Card('heart', 7)
        card2 = Card('diamond', 1)
        cards = [card1, card2]
        self.assertEqual(8 , self.cardgame.cards_total(cards))




       