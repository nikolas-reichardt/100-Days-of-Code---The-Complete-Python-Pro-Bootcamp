from art import logo
import random

def make_guess(attempts, number):
    print(f"You have {attempts} left to guess the number")
    if attempts == 0:
        game_state = "You lost"
    else:
        guess =  int(input("Guess a number: "))
        match guess:
            case g if g < number:
                print("Too low. Guess again")
                attempts -= 1
                game_state = make_guess(attempts, number)
            case g if g > number:
                print("Too high. Guess again")
                attempts -= 1
                game_state = make_guess(attempts, number)
            case g if g == number:
                return "You've got it!"

    return game_state

def start_game(game_mode):
    number = random.randint(1,101)
    print(f"psst: the number is: {number}")
    if game_mode == "easy":
        attempts = 10
    else:
        attempts = 5
    print(make_guess(attempts, number))


while input("Do you want to play again? Type 'y' to play: ") == "y":
    print(logo)
    print("\nWelcome to the number guessing game")
    print("\nGuess a number from 1 to 100")
    start_game(input("Choose a difficulty? Type 'easy' or 'hard': "))

