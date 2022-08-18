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

string_alphabet = 'abcdefghijklmnopqrstuvwxyz '

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        position = string_alphabet.index(char)
        new_position = position + shift_amount
        if new_position > 25:
            cipher_text += string_alphabet[new_position - len(string_alphabet)]
        else:
            cipher_text += string_alphabet[new_position]
    print(f"The encoded text is: {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for char in cipher_text:
        position = string_alphabet.index(char)
        new_position = position - shift_amount
        if new_position < 0:
            plain_text += string_alphabet[len(string_alphabet) + new_position]
        else:
            plain_text += string_alphabet[new_position]
    print(f"The decoded text is: {plain_text}")


if direction.lower() == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction.lower() == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("You can only encode or decode text")
