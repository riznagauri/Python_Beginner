"""
Q. Write a program that takes in a number N as input and does the following:

if N is a multiple of 3, print Fizz
if N is a multiple of 5, print Buzz
if N is a multiple of both 3 and 5, print FizzBuzz
"""

num = int(input('Enter the number: '))

if num % 3 == 0 and num % 5 == 0:
    print('FIZZBUZZ')
elif num % 3 == 0:
    print('FIZZ')
elif num % 5 == 0:
    print('BUZZ')
