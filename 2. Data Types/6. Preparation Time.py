"""
Q. You'll write some code to help you cook a gorgeous lasagna from your favorite cookbook. 
Now, you also want to add a few layers to the lasagna. Assume **each layer takes 2 minutes** to prepare. 
Given the number of layers you want to add to the lasagna, find how many minutes you would spend making them.
"""

num_of_layers = int(input('Enter the number of layers: '))

print('The Lasagna would require {} mins to prepare.'.format(num_of_layers * 2))