"""
Q. Your friend Rahul plans to visit exotic countries all around the world.
Sadly, Rahul's math skills aren't good. He's pretty worried about being scammed
by currency exchanges during his trip - and he wants you to make a currency 
calculator for him. Here are his specifications for the app:

Given the total budget in old currency and the value of a single bill in new currency, 
your need to print the number of new currency bills that you can receive within the given budget.
"""

total_budget = int(input('Enter the Total Budget: '))
bill_value = int(input('Enter the value of a single bill: '))

print('No. of bills that can fit in budget: {}'.format(total_budget // bill_value))