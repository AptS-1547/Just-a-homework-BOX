#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Create a new file named test2.txt which contains the following: 
Teaching at the University of Aberdeen is organised across 12 schools which 
encompass a broad range of disciplines.  
Multidisciplinary research centres and institutes bring together experts at the 
cutting-edge of their fields to work with colleagues across the UK and beyond. 
Create a function which adds a new line to the file created from exercise 4 and 
then adds the text from test2.txt to that file, after the new line.
"""

if __name__ == "__main__":
    with open("./text2.txt", mode="r", encoding="UTF-8") as f:
        add_text = f.read()

    with open("./abdn/text1.txt", mode="a+", encoding="UTF-8") as f:
        f.write("\n" + add_text)
