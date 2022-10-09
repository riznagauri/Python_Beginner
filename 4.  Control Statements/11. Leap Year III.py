"""
Q. 
Given an integer A representing an year, Return 1 if it is a leap year else return 0.

A year is leap year if the following conditions are satisfied:

Year is multiple of 400.
Else the year is multiple of 4 and not multiple of 100.
"""
year = int(input('Enter the year: '))

if year % 400 == 0:
    print('Its a Leap year.')

elif year % 4 == 0 and year % 100 != 0:
    print('Its a Leap year.')

else:
    print('Its not a Leap year.')
