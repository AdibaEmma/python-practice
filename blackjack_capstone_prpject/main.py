import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


user_cards: [int] = []
computer_cards: [int] = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)
