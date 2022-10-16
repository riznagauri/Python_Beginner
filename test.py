"""num = int(input())

total = 0


for i in range(1,num):
    
    total = 0
    print('num {}, total {}'.format(i,total))
    
    for j in range(1,num):
        total += i
        print('i {}, j {}, remainder {}, total {}'.format(i,j,i % j, total))
        if i % j == 0 and total == i:
            print(j, 'is_perfect')
        
    



num = int(input())

total = 0
is_perfect = 'NO'

for j in range(1,num):
    total += j 
    print('j {}, num {}, total {}, remainder {}'.format(j,num,total,num % j))
    if num % j == 0 and total == num:
        is_perfect = 'YES'
        break
    
    
print(is_perfect)
    
"""


A = int(input())

for i in range(A):
    num = int(input())

    total = 0
    is_perfect = 'NO'

    for j in range(1,num):
        total += j 
        if num % j == 0 and total == num:
            is_perfect = 'YES'
            break
        
        
    print(is_perfect)