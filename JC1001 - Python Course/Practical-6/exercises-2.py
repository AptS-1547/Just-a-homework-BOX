#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that combines the two dictionaries below into one and prints it. 
aDict = 
{'Hundred':100,'Ninety':90,'Eighty':80,'Seventy':70,'Sixty': 
60,} 
bDict =  
{'Fifty':50, 'Forty':40, 'Thirty':30, 'Twenty':20, 'Ten':10} 

更多的方法：https://blog.csdn.net/RogerFedereYY/article/details/109544917

"""

aDict = {'Hundred':100,'Ninety':90,'Eighty':80,'Seventy':70,'Sixty': 60}
bDict = {'Fifty':50, 'Forty':40, 'Thirty':30, 'Twenty':20, 'Ten':10} 

new_dict = {}

new_dict.update(aDict)
new_dict.update(bDict)

print(new_dict)