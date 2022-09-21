# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("new_file.txt", mode="w") as file: # Create the file if not exists in write mode
    file.write("New text.")