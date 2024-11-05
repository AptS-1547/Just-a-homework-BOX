#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
A triangle can be classified based on the lengths of its sides as equilateral, 
isosceles or scalene. All 3 sides of an equilateral triangle have the same length. 
An isosceles triangle has two sides that are the same length, and a third side that 
is a different length. If all of the sides have different lengths, then the triangle is 
scalene. Write a program that reads the lengths of 3 sides of a triangle from the 
user. Display a message indicating the type of the triangle.
"""

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
if a == b == c:
    print("The triangle is equilateral")
elif a == b or b == c or a == c:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
