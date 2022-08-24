import random
from art import logo

print(logo)
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
random_number = round(random.random() * 100)


def set_attempts(difficulty_level):
    if difficulty_level == "easy":
        return attempts + 10
    elif difficulty_level == "hard":
        return attempts + 5


attempts = set_attempts(difficulty_level=level)

print(f"You have {attempts} attempts remaining to guess the number")


def get_response(msg: str, attempts_left: int):
    print(f"{msg}.")
    print("Guess again.")
    print(f"You have {attempts_left} attempts remaining to guess the number")


guessed_right = False

while not guessed_right and attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == random_number:
        guessed_right = True
        print("You guessed right.")
    elif guess > random_number:
        attempts -= 1
        get_response("Too High", attempts)
    elif guess < random_number:
        attempts -= 1
        get_response("Too low", attempts)

print(random_number)
