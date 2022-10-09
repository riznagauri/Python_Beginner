"""
Q. You have been given a dataset for marks of 2 subjects, scored by students of classes ClassA and ClassB. 
You now want to compare the performances of class A and class B by finding out the average performance of the classes. 
Write a program to find if class A performed better.
Print which class is better.
"""
classA_sub1 = int(input('Enter marks of class A subject 1: '))
classA_sub2 = int(input('Enter marks of class A subject 2: ')) 
classB_sub1 = int(input('Enter marks of class B subject 1: '))
classB_sub2 = int(input('Enter marks of class B subject 2: '))

avg_classA = (classA_sub1 + classA_sub2) / 2
avg_classB = (classB_sub1 + classB_sub2) / 2

if avg_classA > avg_classB:
    print('Class A performance is better.')
else:
    print('Class B performance is better.')