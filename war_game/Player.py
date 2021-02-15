class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards.'

    def remove_one(self):
        return self.cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of several Card objects
            self.cards.extend(new_cards)
        else:
            # single Card object
            self.cards.append(new_cards)


p = Player("player 1")
print(p)
p.add_cards([1, 2, 3, 4])
print(p)
p.remove_one()
print(p)