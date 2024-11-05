#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program which converts miles into kilometres. Your program should first 
ask the user to enter a distance in miles to be converted and you should then 
return the converted distance in kilometres. Include in the output, the original 
value in miles that has been converted into kilometres. (1 kilometre is 
approximately 0.6214 miles) 
"""

distance = int(input("Please enter an length in miles: "))

print(f"Length is {distance} miles and convert in kilometres is {distance/0.6214}")