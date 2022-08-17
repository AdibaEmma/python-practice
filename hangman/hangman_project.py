import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}')
display = []
for _ in chosen_word:
    display.append('_')

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose.")



    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You won!")
    print(stages[lives])


