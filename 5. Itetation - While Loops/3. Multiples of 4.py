"""
Q. Given an integer input N, print all multiples of 4 less than or equal to N.
"""

N = int(input('Enter the integer: '))

num = 1 

while num * 4 <= N:
    print(num * 4, end= ' ')

    num += 1
