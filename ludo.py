import random

#Dice code
lst = []
Using = 'yes'
while Using.lower() == 'yes':
    x = random.randint(1,6)
    print(x)
    lst.append(x)
    Using = input('Yes to continue: ')
    
print(lst)
