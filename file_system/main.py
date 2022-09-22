# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", mode="w") as file: # Create the file if not exists in write mode
#     file.write("New text.")

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as file:
    names_to_invite = file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_contents = file.readlines()
    for name in names_to_invite:
        formatted_name = name.strip("\n")
        greetings = letter_contents[0].replace("[name]", f"{formatted_name}")
        with open(f"./Output/ReadyToSend/{formatted_name.lower()}.txt", "w") as file:
            for content in letter_contents:
                if content == letter_contents[0]:
                    content = greetings
                file.write(content)
