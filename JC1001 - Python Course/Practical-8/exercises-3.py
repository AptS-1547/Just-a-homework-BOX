#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Create function which calculates the number of occurrences / word frequency of 
the word “Aberdeen”
"""

def count_occurrences(text, word):
    if not text or not word:
        return 0

    position = 0
    count = 0
    while (word in text):
        position = text.find(word)
        text = text[position + len(word) :]
        count +=1
    
    return count

if __name__ == "__main__":
    with open("./text1.txt", encoding="utf-8", mode="r") as f:
        text = f.read()
        word = "Aberdeen"
        frequency = count_occurrences(text, word)
        print(f"The word '{word}' occurs {frequency} times.")
