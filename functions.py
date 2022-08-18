# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with(name="Emma", location="Bolga")

from math import ceil

#
# def paint_calc(height, width, cover):
#     area = height * width
#     paint_cans = ceil(area / cover)
#     print(f"You'll need {paint_cans} cans of paint.")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
# paint_calc(height=test_h, width=test_w, cover=coverage)


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
#
#
# n = int(input("Check this number: "))
# prime_checker(n)

alphabet = 'abcdefghijklmnopqrstuvwxyz '

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        position = alphabet.index(char)
        if cipher_direction.lower() == "encode":
            new_position = position + shift_amount
            if new_position > 25:
                end_text += alphabet[new_position - len(alphabet)]
            else:
                end_text += alphabet[new_position]
        elif cipher_direction.lower() == "decode":
            new_position = position - shift_amount
            if new_position < 0:
                end_text += alphabet[new_position + len(alphabet)]
            else:
                end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

