from Deck import Deck
from Player import Player

round = 0
game_on = True
player_1 = Player("One")
player_2 = Player("Two")
deck = Deck()
deck.shuffle_deck()

for i in range(26):
    player_1.add_cards(deck.deal_one())
    player_2.add_cards(deck.deal_one())

print(player_1.cards[0])
print(player_2.cards[0])

while game_on:
    round += 1
    print(f"Round {round}")

    # check if players are out of cards
    if len(player_1.cards) == 0:
        print(f"Player {player_1.name} out of cards! Player {player_2.name} wins!")
        game_on = False
        round = 0
        break
    if len(player_2.cards) == 0:
        print(f"Player {player_2.name} out of cards! Player {player_1.name} wins!")
        game_on = False
        round = 0
        break

    # if players still have cards, start a new round
    player_1_table_cards = []
    player_1_table_cards.append(player_1.remove_one())
    player_2_table_cards = []
    player_2_table_cards.append(player_2.remove_one())

    at_war = True
    while at_war:
        if player_2_table_cards[-1].value > player_1_table_cards[-1].value:
            player_2.add_cards(player_2_table_cards)
            player_2.add_cards(player_1_table_cards)
            at_war = False
            break
        elif player_1_table_cards[-1].value > player_2_table_cards[-1].value:
            player_1.add_cards(player_1_table_cards)
            player_1.add_cards(player_2_table_cards)
            at_war = False
            break
        else:
            print("War!")
            if len(player_1.cards) < 3:
                print(f"Player {player_1.name} cannot declare a war!")
                print(f"Player {player_2.name} wins!")
                game_on = False
                round = 0
                break
            elif len(player_2.cards) < 3:
                print(f"Player {player_2.name} cannot declare a war!")
                print(f"Player {player_1.name} wins!")
                game_on = False
                round = 0
                break
            else:
                for i in range(3):
                    player_1_table_cards.append(player_1.remove_one())
                    player_2_table_cards.append(player_2.remove_one())