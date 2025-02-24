#!/usr/bin/env python3

"""
A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function 
that determines whether or not its parameter is prime, returning True if it is, and False otherwise. 
Write a main program that reads an integer from the user and displays a message indicating 
whether or not it is prime. Ensure that the main program will not run if the file containing your 
solution is imported into another program.
"""

def prime(num: int) -> bool:
    if num < 2: return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()