import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat",
             "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck",
             "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk", "lion", "lizard",
             "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl",
             "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven", "rhino",
             "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider", "stork",
             "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf",
             "wombat", "zebra"]

chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}')
display = []
for _ in chosen_word:
    display.append('_')

print(display)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You won!")
    print(stages[lives])


