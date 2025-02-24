#!/usr/bin/env python3

"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees
Fahrenheit. The table should include rows for all temperatures between 0 and 100 degrees Celsius
that are multiples of 10 degrees Celsius. Include appropriate headings on your columns. The
formula for converting between degrees Celsius and degrees Fahrenheit is:
T (°F) = T (°C) × 9/5 + 32
"""
print("Celsius\tFahrenheit")
for celsius in range(0, 101, 10):
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}\t{fahrenheit}")