"""
Q. Your friend Rahul plans to visit exotic countries all around the world. Sadly, 
Rahul's math skills aren't good enough. He's pretty worried about being scammed by 
currency exchanges during his trip - and he wants you to make a currency calculator for him. 
Given the amount of money Rahul has before the exchange and the amount of money that is spent from his savings,
Print the amount of money that remains in his savings.
"""

total_savings = int(input('Enter total saved amount: '))
spent_amount = int(input('Enter spent amount: '))

print('Balance amount: Rs. {}'.format(total_savings - spent_amount))