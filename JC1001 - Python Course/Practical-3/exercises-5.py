#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that determines the name of a shape from its number of sides. 
Read the number of sides from the user and then report the appropriate name as 
part of a meaningful message. Your program should support shapes with 
anywhere from 3 up to (and including) 10 sides. If the number of sides outside of 
this range is entered, then your program should display an appropriate error 
message. 
"""

sides = int(input("Enter the number of sides: "))

if sides == 3:
    print("It is a triangle.")
elif sides == 4:
    print("It is a quadrilateral.")
elif sides == 5:
    print("It is a pentagon.")
elif sides == 6:
    print("It is a hexagon.")
elif sides == 7:
    print("It is a heptagon.")
elif sides == 8:
    print("It is an octagon.")
elif sides == 9:
    print("It is a nonagon.")
elif sides == 10:
    print("It is a decagon.")
else:
    print("Invalid number of sides. Please enter a number between 3 and 10.")
