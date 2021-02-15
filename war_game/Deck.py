from card import Card
from random import shuffle


values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
suites = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")


class Deck:
    def __init__(self):
        self.deck = []
        for suite in suites:
            for rank in ranks:
                # create a new card and add it to the deck
                self.deck.append(Card(rank, suite))

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

d = Deck()
d.shuffle_deck()
for card in d.deck:
    print(card)
card = d.deal_one()
print()
print(card)
card = d.deal_one()
print(card)

