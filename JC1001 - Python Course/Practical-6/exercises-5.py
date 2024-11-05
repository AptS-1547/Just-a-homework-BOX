#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program for the task in exercise 3 using dictionary comprehension. If you 
have already used dictionary comprehension previously, write the program using 
a for loop.

Tasks3:
Write a program that creates a new dictionary by extracting specific keys from 
another dictionary. Below is an example dictionary you can use and a list 
containing the specific keys we want to extract to create our new dictionary. 
Remember to print the new dictionary created. 
userProfile = { 
"name": "JP", 
"age":  "25 :)", 
"number of cats": 12, 
"city": "Bristol" 
} 
theKeysIwant = ["name","number of cats"]

"""

userProfile = { 
"name": "JP", 
"age":  "25 :)", 
"number of cats": 12, 
"city": "Bristol" 
} 
theKeysIwant = ["name","number of cats"]

new_dict = {key: value for key, value in userProfile.items() if key in theKeysIwant}

print(new_dict)
