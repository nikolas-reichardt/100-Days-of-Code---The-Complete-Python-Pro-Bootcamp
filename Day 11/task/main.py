import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand= []
computer_hand = []
new_card = True
game_over = False

input("Do you want to play Blackjack? Type 'y' or 'n': ")
print(f"\n {logo} \n")

user_hand.append(random.choice(cards))
user_hand.append(random.choice(cards))

print(f"Your current cards are [{user_hand}], current score: {sum(user_hand)}")

computer_hand.append(random.choice(cards))

print(f"Computer's first card: [{user_hand[0]}]")



while new_card:
    if sum(user_hand) <= 21:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
            new_card = False
            print(f"Your final cards are {user_hand}, current score: {sum(user_hand)}")
        else:
            user_hand.append(random.choice(cards))
            print(f"Your cards are {user_hand}, current score: {sum(user_hand)}")

    else:
        new_card = False
        game_over = True

while sum(user_hand) > sum(computer_hand) and not game_over and not sum(computer_hand) == 21 and not sum(user_hand) == 21:
    computer_hand.append(random.choice(cards))
    print(f"Computer's cards are {computer_hand}, current score: {sum(computer_hand)}")

if sum(user_hand) > sum(computer_hand) and not game_over and sum(computer_hand) <= 21:
    print(f"You won: Your final cards are {user_hand}, current score: {sum(user_hand)}")
else:
    print(f"You lost: Your final cards are {user_hand}, current score: {sum(user_hand)}")