#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that converts the two lists below into a dictionary and prints the 
dictionary.  
wNum = ['Fifty','Forty','Thirty','Twenty','Ten'] 
wVal = [50,40,30,20,10] 
"""

wNum = ['Fifty','Forty','Thirty','Twenty','Ten']
wVal = [50,40,30,20,10] 

num_dict = dict(zip(wNum, wVal))

print(num_dict)
