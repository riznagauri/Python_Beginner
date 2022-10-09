"""
Q. You wrote some code to help you cook a gorgeous lasagna from your favorite cookbook. 
Now, you want to find the total number of minutes you've been cooking or the sum of your 
preparation time and the time the lasagna has already been spent baking in the oven. 
The preparation time of one layer is 2 minutes. Given the number of layers added to the 
lasagna and the number of minutes the lasagna has been baking in the oven, 
find the total elapsed cooking time (prep + bake) in minutes.
"""

from re import M


num_of_layers = int(input('Enter number of layers: '))
baked_time = int(input('Enter the already baked time: '))

print('Total elapsed cooking time is: {} mins'.format(baked_time + num_of_layers * 2))