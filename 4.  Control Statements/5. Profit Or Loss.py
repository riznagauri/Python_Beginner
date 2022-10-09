"""
Q. You are given the Cost Price C and Selling Price S of a Product. 
You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss. 
Note: It is guaranteed that Cost Price and Selling Price are not equal.
"""
cost_price = int(input('Enter Cost price: '))
selling_price = int(input('Enter Selling price: '))

if selling_price > cost_price:
    print('Its a Profit of Rs. {}'.format(selling_price - cost_price))

else:
    print('Its a Loss of Rs. {}'.format(cost_price - selling_price))
