import art
from game_data import data
import random

def is_higher_or_lower(input, a, b):
    if a["follower_count"] > b["follower_count"]:
        return input == "a"
    else:
        return input == "b"

#def user_choice(choice):
#    return

def start_game():
    compare_b = data[random.randint(0, len(data))]
    print(art.logo)
    game_over = False
    score = 0
    while not game_over:
        compare_a = compare_b
        compare_b = data[random.randint(0,len(data))]
        if compare_a == compare_b:
            compare_b = data[random.randint(0, len(data))]
        print(f"Compare A: {compare_a["name"]}, {compare_a["description"]}, from {compare_a["country"]}")
        print(art.vs)
        print(f"Compare B: {compare_b["name"]}, {compare_b["description"]}, from {compare_b["country"]}")
        game_over = is_higher_or_lower(input("Who has more followers? Type 'A' or 'B'").lower(), compare_a, compare_b)
        if not game_over:
            score += 1
            print(f"You're right. Current score {score}.")
        else:
            print(f"You're wrong. Final score {score}.")

start_game()