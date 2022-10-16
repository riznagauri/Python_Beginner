"""
Q. Problem Description

Write a program to print all Natural numbers from N to 1 where you have to take N as input from user
"""

N = int(input('Enter the last number: '))

for i in range(N, 0, -1):
    print(i, end= ' ')
