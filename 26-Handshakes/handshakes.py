"""
Write a function named print_hand_shakes() with a list parameter named people which will
be a list of strings of people’s names. The function prints out 'X shakes hands with Y', where
X and Y are every possible pair of handshakes between the people in the list. No duplicates are
permitted: if ―Alice shakes hands with Bob‖ appears in the output, then ―Bob shakes hands with
Alice‖ should not appear.
For example, printHandshakes(['Alice', 'Bob', 'Carol', 'David']) should
print:
Alice shakes hands with Bob
Alice shakes hands with Carol
Alice shakes hands with David
Bob shakes hands with Carol
Bob shakes hands with David
Carol shakes hands with David
The printHandshakes() function must also return an integer of the number of handshakes.
"""

def print_hand_shakes(people):
    count = 0

    for i in range(0, len(people) - 1):
        for j in range(i + 1, len(people)):
            count += 1
            print(f"{people[i]} shakes hands with {people[j]}")

    return count

assert print_hand_shakes(['Alice', 'Bob']) == 1
assert print_hand_shakes(['Alice', 'Bob', 'Carol']) == 3
assert print_hand_shakes(['Alice', 'Bob', 'Carol', 'David']) == 6
