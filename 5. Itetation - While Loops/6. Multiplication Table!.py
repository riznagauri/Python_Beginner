"""
Q. Problem Description
For a given number A, print its multiplication table having the first 10 multiples.
"""

A = int(input('Enter the number for who\'s table want: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(A, i, A * i))