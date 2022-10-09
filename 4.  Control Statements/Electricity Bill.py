"""
Q. Generate electricity bill using the following rate card. Take units consumed as input -

If < 100 units -> Free
If >= 100 units and < 200 units -> Rs 2 per unit
If >= 200 units -> Rs 5 per unit
print the final amount

"""
units_used = int(input('Enter the units comsumed: '))

if units_used < 100:
    print('No charges. Its Free!')

elif 100 <= units_used < 200:
    print('Electricity bill amount is: Rs. {}'.format(units_used * 2))

elif units_used >= 200:
    print('Electricity bill amount is: Rs. {}'.format(units_used * 5))