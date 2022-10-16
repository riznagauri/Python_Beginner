"""
Q. Problem Description
Mr. Q has a diary in which a lot of numbers are written. 
He wants to know the sum of digits for every number. 
First Ask Mr. Q about the numbers written in the diary and 
then write a code to find the sum of digits for every number.
Note: Total different Numbers are T and for every number (let's say N) you need to find the Sum of digits.
"""
T = int(input('Mr. Q, Enter the total numbers written in your dairy: '))

for i in range(T):
    num = int(input('Enter number {}: '.format(i+1)))

    total = 0
    while num != 0:
        digit = num % 10

        total += digit

        num //= 10
    
    print('Sum of digit(s) in number {} is: {}'.format(i+1, total))

