"""
Q. Problem Description
Mr. Q has a diary in which he has written a lot of numbers.
He is confused about the number of digits in every number he has written.
Mr. Q will provide the different numbers written in the diary and
then you have to write a code to find the number of digits in every number he has written.

Note: Total different Numbers are T and for every number (let's say N) you need to find the total number of digits.
"""

T = int(input('Mr. Q, Enter the total numbers written in your dairy: '))

for i in range(T):
    num = int(input('Enter number {}: '.format(i+1)))

    count = 0
    while num != 0:
        digit = num % 10

        count += 1

        num //= 10
    
    print('Number of digit(s) in number {} is/are: {}'.format(i+1, count))