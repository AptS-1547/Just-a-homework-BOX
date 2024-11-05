#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function which creates a directory named “abdn” and copies the text file 
text1.txt to the new directory and then prints the contents of the director. Note, 
use the shutil and os module methods to help.
"""

import os, shutil

if __name__ == "__main__":
    if not os.path.exists("./abdn"):
        os.mkdir("./abdn")
    
    if os.path.exists("./text1.txt") and not os.path.exists("./abdn/text1.txt"):
        shutil.copyfile("./text1.txt", "./abdn/text1.txt")
    else:
        print("already exist or file not found")

    with open("./abdn/text1.txt", mode="r", encoding="UTF-8") as f:
        print(f.read())
