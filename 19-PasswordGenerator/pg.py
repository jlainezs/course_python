"""
Write a generate_password() function that has a length parameter. The length
parameter is an integer of how many characters the generated password should have. For security
reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway.
The password string returned by the function must have at least

one lowercase letter
one uppercase letter
one number
one special character.

The special characters for this exercise are ~!@#$%^&*()_+.
Your solution should import Python’s random module to help randomly generate these
passwords.
"""

import random

special = "~!@#$%^&*()_+"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
def pick_random_character(characters):
    return random.choice(characters)

def generate_password(length):
    use_length = 12 if length < 12 else length
    generated_password = [pick_random_character(special),
                          pick_random_character(lower),
                          pick_random_character(upper),
                          pick_random_character(numbers)
                         ]

    for i in range(use_length - 4):
        generated_password.append(pick_random_character(special + lower + upper + numbers))

    random.shuffle(generated_password)

    return "".join(generated_password)

assert len(generate_password(8)) == 12
pw = generate_password(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in lower:
        hasLowercase = True
    if character in upper:
        hasUppercase = True
    if character in numbers:
        hasNumber = True
    if character in special:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
