"""
Q. Problem Description

Write a program to find sum of all Natural numbers from 1 to N where you have to take N as input from user
"""

N = int(input('Enter the last number: '))

total = 0

for i in range(1, N+ 1):
    total += i

print('The sum of all natural numbers from 1 to {} is: {}'.format(N, total))

