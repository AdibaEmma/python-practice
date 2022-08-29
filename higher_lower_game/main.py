from art import logo, vs
from game_data import data


print(logo)
guessed_right = True
score = 0
i = 0

while guessed_right:
    optionA = data[i]
    print(f"Compare A: {optionA['name']}, {optionA['description']}")
    print(vs)
    optionB = data[i + 1]
    print(f"Against B: {optionB['name']}, {optionB['description']}")

    chosen_option = input("Who has more followers? Type 'A' or 'B': ")

    if chosen_option == "A":
        if optionA["follower_count"] > optionB["follower_count"]:
            score += 1
            i += 1
        else:
            guessed_right = False
            print(f"Sorry, that's wrong. Final score: {score}")
    elif chosen_option == "B":
        if optionB["follower_count"] > optionA["follower_count"]:
            score += 1
            i += 1
        else:
            guessed_right = False
            print(f"Sorry, that's wrong. Final score: {score}")
