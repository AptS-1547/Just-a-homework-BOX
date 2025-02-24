#!/usr/bin/env python3

"""
In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her 
ticket to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program 
that generates a random selection of 6 numbers for a lottery ticket. Ensure that the 6 numbers 
selected do not contain any duplicates. Display the numbers in ascending order. 
"""

import random

def main():
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
        else:
            continue
    numbers.sort()
    print(numbers)

if __name__ == "__main__":
    main()