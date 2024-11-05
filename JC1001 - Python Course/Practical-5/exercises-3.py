#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Rewrite the function from exercise 2 to use list comprehension. If you have 
already used list comprehension, rewrite the function to use a for loop.
"""

def only_odd_number(list_num: list) -> list:
    list_odd = [ num for num in list_num if num % 2 == 1]

    return list_odd

print(only_odd_number(range(1,1000)))
