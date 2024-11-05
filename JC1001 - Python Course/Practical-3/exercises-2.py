#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that reads a letter from the English alphabet from the user. If the 
letter is a vowel (a,e,i,o,u) then it should inform the user that it is a vowel. If the 
user enters a (y), then the user should be informed that a y can sometimes be a 
vowel and sometimes is not. For all other input letters, the program should inform 
the user that it is a consonant. 
"""

VOWEL = ("a", "e", "i", "o", "u")

letter = input("Please enter a letter from the English alphabet: ")

if letter in VOWEL:
    print(letter, "it is a vowel")
elif letter == "y":
    print("y can sometimes be a vowel and sometimes is not")
else:
    print(letter, "it is a consonant")