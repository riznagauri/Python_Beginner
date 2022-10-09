"""
Q. Write a program to input two numbers(A & B) from user and 
print the minimum element among A & B in each line.
"""

A = int(input('Enter 1st number: '))
B = int(input('Enter 2nd number: '))

if A < B:
    print('{} is minimum'.format(A))
else:
    print('{} is minimum'.format(B))

