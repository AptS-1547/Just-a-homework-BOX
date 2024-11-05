#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function that receives a list of integers and returns a new list using list 
comprehension to calculate the square of each element if the square of each 
element is > 50.
"""

def square_list_num(list_num: list) -> list:
    return [ num**2 for num in list_num if num > 50 ]

print(square_list_num(range(1,101)))
