"""
Q. Build a meter system for an auto. Take into two inputs. Kilometers Travelled and Stall Time (in minutes). Rate List -

First 10 kms - Rs 10 per Km
Next 40 kms - Rs 9 per Km
Next 100 kms - Rs 8 per Km
Any leftover km count - Rs. 6 per Km
Rs 5 extra for every minute of Stall Time
print the final fare
"""

fare = 0 # Initilizing fare at starting point

km_travelled = int(input('Enter the distaince travelled in km: '))
stall_time = int(input('Enter Stall time in mins.: '))

if km_travelled <= 10: # Checking if Km is less than 10 
    fare = km_travelled * 10 
    #print('10 fare',fare)
else:
    fare += 10 * 10 # Since fare is more than 10, adding fare @ 10km rate
    #print('10 fare',fare)
    distance40 = km_travelled - 10 # 10km accounted for, deducting it to calculate further fare.

    if distance40 <= 40:
        fare += distance40 * 9
        #print('40 fare',fare)
    else:
        fare += 40 * 9
        #print('40 fare',fare)
        distance100 = distance40 - 40

        if distance100 <= 100:
            fare += distance100 * 8
            #print('100 fare',fare)
        else:
            fare += 100 * 8
            #print('100 fare',fare)
            left_distance = distance100 - 100
            fare += left_distance * 6
            #print('left fare',fare)

fare += stall_time * 5 # Adding stalling time charges.


print('Final auto fare is: Rs. {}'.format(fare))
