#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that asks the user for the length and width of two rooms. It 
should then inform the user whether the areas are the same, or if not, which room 
is larger.
"""

length1 = float(input("Enter the length of the first room: "))
width1 = float(input("Enter the width of the first room: "))
area1 = length1 * width1

length2 = float(input("Enter the length of the second room: "))
width2 = float(input("Enter the width of the second room: "))
area2 = length2 * width2

if area1 == area2:
    print("The areas of the two rooms are the same.")
elif area1 > area2:
    print("The first room is larger.")
else:
    print("The second room is larger.")