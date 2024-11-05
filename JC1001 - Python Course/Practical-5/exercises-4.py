#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function that receives a list of integers and returns a new list using list 
comprehension which contains each item from the original list, multiplied by 10.
"""

def list_multiplied_ten(list_num: list) -> list:
    return [ num*10 for num in list_num]

print(list_multiplied_ten(range(1,1000)))
