"""
ROT 13 is a simple encryption cipher. The name ―ROT 13‖ is short for ―rotate 13.‖ It encrypts by
replacing letters with letters that appear 13 characters down the alphabet: A is replaced with N, B is
replaced with O, C is replaced with P, and so on. If this rotation of 13 letters goes passed the end of
the alphabet, it ―wraps around‖ the Z and continues from the start of the alphabet. Thus, X is
replaced with K, Y is replaced with L, Z is replaced with M, and so on. Non-letter characters are left
unencrypted.
The benefit of ROT 13 is that you can decrypt the encrypted text by running it through ROT 13
encryption again. This rotates the letter 26 times, returning us to the original letter. So ―Hello, world!‖
encrypts to ―Uryyb, jbeyq!‖ which in turn encrypts to ―Hello, world!‖ There is no decryption
algorithm; you decrypt encrypted text by encrypting it again. The ROT 13 algorithm isn’t secure for
real-world cryptography. But it can be used to obfuscate text to prevent spoiling joke punch lines or
puzzle solutions.
Write a rot13() function with a text parameter that returns the ROT 13 encrypted version of
text. Uppercase letters encrypt to uppercase letters and lowercase letters encrypt to lowercase letters.
For example, 'HELLO, world!' encrypts to 'URYYB, jbeyq!' and 'hello, WORLD!'
encrypts to 'uryyb, JBEYQ!'.
You may use the following Python functions and string methods as part of your solution: ord(),
chr(), isalpha(), islower(), and isupper().
"""
def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            rotated = ord(char) + 13
            if char.islower() and rotated > 122: # 122 = 'z'
                rotated -= 26
            if char.isupper() and rotated > 90: # 90 = 'Z'
                rotated -= 26
            rotated_char = chr(rotated)
            result += rotated_char
        else:
            result += char

    return result

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'