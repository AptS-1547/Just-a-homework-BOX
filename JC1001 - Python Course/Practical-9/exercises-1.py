#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a recursive function that calculates and return the sum of a list of 
numbers
"""

def sum_recursive(numbers):

    if not numbers:
        return 0

    return numbers[0] + sum_recursive(numbers[1:])

if __name__ == "__main__":
    numbers = [114514, 1919810, 1, 3, 5, 7, 15470, 25565]
    result = sum_recursive(numbers)
    print(f"The sum of the list is: {result}")