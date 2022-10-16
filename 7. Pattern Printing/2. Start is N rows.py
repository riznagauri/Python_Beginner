"""
Q 1. Write a program to print:

*
**
***
****
*****

take n as input
"""

N = int(input('Enter number of rows for partern: '))

for i in range(N):
    for j in range(i + 1):
        print('*', end = '')
    print()