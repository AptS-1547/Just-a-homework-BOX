#!/usr/bin/env python3

"""
A string is a palindrome if it is identical forward and backward. For example, “anna”, “civic”, “level” 
and “hannah” are all examples of palindromic words. Write a program that reads a string from the 
user and uses a loop to determines whether or not it is a palindrome. Display the result, including a 
meaningful output message. 
"""

string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")