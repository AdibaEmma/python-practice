import random
#
# random_integer = random.randint(1, 10)
#
# random_float = round(random.random() * 5)
# print(random_float)

# names_string = input("Give me everybody's name, seperated by a comma. ")
# names = names_string.strip().split(",")
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meal today!")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_input = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_input >= len(game_input):
    print("You entered an invalid number, you lose!")
else:
    user_choice = game_input[user_input]
    computer_choice = random.choice(game_input)
    print(user_choice)
    print(f"Computer chose: {computer_choice}")
    if user_input == 0 and game_input.index(computer_choice) == 2 or user_input > game_input.index(computer_choice):
        print("You win!")
    elif game_input.index(computer_choice) > user_input:
        print("Computer wins!")
    elif user_input == game_input.index(computer_choice):
        print("It's a draw!")
    else:
        print("You entered an invalid number, you lose!")
