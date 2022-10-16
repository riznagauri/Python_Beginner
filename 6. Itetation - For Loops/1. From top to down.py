"""
Q. Problem Description

Write a program to print all Natural numbers from 1 to N where you have to take N as input from user.
"""

N = int(input('Enter the last natural number you want: '))

print('Natural numbers from 1 to {} are: '.format(N))

for i in range(1, N + 1):
    print(i, end = ' ')