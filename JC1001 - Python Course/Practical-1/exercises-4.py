#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks: Write a program that asks the user to enter first their height in feet, followed by 
the number of inches e.g. first the user may enter 5, followed by 8, meaning their 
height is 5 feet, 8 inches. Your program should then return the user’s height in 
centimetres"""

feet, inches = input("Please enter your height in feet and inches, using space spacing: ").split()

print(f"Your height is {int(feet)*30.48 + int(inches)*2.54} centimetres")
