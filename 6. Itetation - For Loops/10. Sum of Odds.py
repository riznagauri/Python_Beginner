"""
Q. Problem Description

You are given a positive integer A as input. You have to print the sum of all odd numbers in the range [1, A].
"""

A = int(input("Enter the number: "))

total = 0

for i in range(1, A + 1):
    if i % 2 != 0:
        
        total += i

print('Sum of all Odd number is range [1, {}] is: {}'.format(A, total))
