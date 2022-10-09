"""
Q. Your friend Rahul plans to visit exotic countries all around the world. 
Sadly, Rahul's math skills aren't good. He's pretty worried about being scammed 
by currency exchanges during his trip - and he wants you to make a currency calculator for him. 
Here are his specifications for the app:
Given the value of a single bill and the number of bills you received, print the total value of the bills.
"""

bill_value = int(input('Enter bill value: '))
num_of_bills = int(input('Enter number of bills: '))

print('Total value of the bills: Rs. {}'.format(bill_value * num_of_bills))
