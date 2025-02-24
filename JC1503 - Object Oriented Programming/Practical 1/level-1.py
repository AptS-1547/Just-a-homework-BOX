#!/usr/bin/env python3

"""
Write a program that asks the user to enter the width and length of a room. Once the values have 
been read, your program should compute and display the area of the room. The length and the 
width will be entered as floating point numbers. Include units in your prompt and output message; 
either feet or metres, depending on which unit you are more comfortable working with. 
"""

(width, length) = input("Enter the width and length of the room in feet, using a space to separate the two values: ").split()
width = float(width)
length = float(length)

area = width * length
print(f"The area of the room is {area} square feet.")