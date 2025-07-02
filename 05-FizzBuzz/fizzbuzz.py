"""
Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1
up to and including upTo, the function prints one of four things:

- Prints 'FizzBuzz' if the number is divisible by 3 and 5.
- Prints 'Fizz' if the number is only divisible by 3.
- Prints 'Buzz' if the number is only divisible by 5.
- Prints the number if the number is neither divisible by 3 nor 5.

Instead of printing each string or number on a separate line, print them without newlines. For
example, your solution is correct if calling fizzBuzz(35) produces the following output:
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22
23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz

"""

def fizz_buzz(up_to):
    for i in range(1, up_to + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

fizz_buzz(35)