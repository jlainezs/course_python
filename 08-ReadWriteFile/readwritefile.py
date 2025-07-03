"""
You will write three functions for this exercise.
First, write a writeToFile() function with
two parameters for the filename of the file and the text to write into the file.
Second, write an appendToFile() function, which is identical to writeToFile()
except that the file opens in append mode instead of write mode.
Finally, write a readFromFile() function with one parameter
for the filename to open. This function returns the full text contents of the file as a string.
"""

def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

write_to_file('greet.txt', 'Hello!\n')
append_to_file('greet.txt', 'Goodbye!\n')
assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'
