"""
Q. A programmer for a music company is developing a program to determine the highest level of certification for an album.
The program needs to follow this table of thresholds for each certification level:

Minimum albums sold	Certification
500000 --> gold
1000000	--> platinum
10000000 --> diamond
Given the albums sold(N) as input, print the certification for the album.
"""

albums_sold = int(input('Enter the number of albums sold: '))

if 0 < albums_sold < 500000:
    print('None')

elif 500000 <= albums_sold < 1000000:
    print('gold')

elif 1000000 <= albums_sold < 10000000:
    print('platinum')

elif albums_sold >= 10000000:
    print('diamond')
