#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Create a text file that contains the following text and name the file test1.txt 

The University of Aberdeen is a public research university in Aberdeen, 
Scotland.  
It is an ancient university founded in 1495 when William Elphinstone, Bishop of  
Aberdeen and Chancellor of Scotland petitioned Pope Alexander VI on behalf of  
James IV, King of Scots to establish King's College making it Scotland's  
third-oldest university and the fifth-oldest in the English-speaking world. 

Write a function which reads the text file and prints its content.
"""

with open("./text1.txt", encoding="utf-8", mode="r") as f:
    print(len(f.read().replace("  ", " ").replace("\n", "").split(" ")))
    
