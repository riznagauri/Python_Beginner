"""
Q. You are given an integer A.

You have to tell how many days are there in the month denoted by A in a non-leap year.
"""

month_num = int(input('Enter number for the month: '))

if month_num == 2:
    print(28)
elif 0 < month_num < 8 and month_num % 2 != 0:
    print(31)
elif 8 <= month_num <= 12 and month_num % 2 == 0:
    print(31)
elif 0 < month_num < 8 and month_num % 2 == 0:
    print(30)
elif 8 < month_num < 12 and month_num % 2 != 0:
    print(30)
