#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program for the task in exercise 4 using dictionary comprehension.  If you 
have already used dictionary comprehension previously, write the program using 
a for loop.

Tasks4:
Write a program that removes specific keys from a dictionary and prints the 
dictionary after it has been modified. You may create your own dictionary or use 
the following example: 
userProfile = { 
"name": "JP", 
"age":  "25 :)", 
"number of cats": 12, 
"city": "Bristol" 
} 
theKeysIwantToRemove = ["age","city"] 

"""

userProfile = { 
"name": "JP", 
"age":  "25 :)", 
"number of cats": 12, 
"city": "Bristol" 
} 
theKeysIwantToRemove = ["age","city"] 

new_dict = {key: value for key, value in userProfile.items() if key not in theKeysIwantToRemove}

print(new_dict)
