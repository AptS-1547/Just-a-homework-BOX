#!/usr/bin/env python3

"""
The Chinese zodiac assigns animals to years in a 12-year cycle. One 12-year cycle is shown in the 
table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 
being another year of the hare. 
 
Year Animal 
2000  Dragon 
2001  Snake 
2002  Horse 
2003  Sheep 
2004  Monkey 
2005  Rooster 
2006  Dog 
2007  Pig 
2008  Rat 
2009  Ox 
2010  Tiger 
2011  Hare 
 
Write a program that reads a year from the user and displays the animal associated with that year. 
Your program should work correctly for any year greater than or equal to zero, not just the ones 
listed in the table. 
"""

year = int(input("Enter the year: "))
animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]
print(f"The animal associated with the year {year} is {animals[(year - 2000) % 12]}")