##my_list = [1, 2, 3, 4, 5]
##print(len(my_list))
##
##list1 = ['a', 'b', 'c', 'd', 'e']
##print(list1[-1])
##print(list1[4])
##
##
##letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
##sublist = letters[1:6]
##print(sublist)
##
##letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
##num_i = letters.count('i')
##print(num_i)
##
##
##names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
##print(names)
##
##names.sort()
##print(names)
##
##
##sorted_names = names.sort()
##print(sorted_names)

def List():
    lst = []
    Using = 'yes'
    while Using.lower() == 'yes':
        temp = input("enter list item: ")
        lst.append(temp)
        Using = input("Enter yes to continue: ")
    print(lst)
    return lst

def Sel_List(lst):
    Using = 'yes'
    while Using.lower() == 'yes':
        Id_val = int(input("What index value? "))
        print(lst[Id_val])
    return lst

def Slicing_List(lst):
    lst = []
    Using = 'yes'
    while Using.lower() == 'yes':
        temp = input("enter list item: ")
        Using = input("Enter yes to continue: ")
    
    index = int(input("index value of start of split: "))
    value = input("index value of end of split:  ")
    sublist = lst[index:value]
    print(lst)
        
    return lst


lst =[]
Using = 'yes'
while Using == 'yes':
    print('enter 1 to create. \n enter 2 to sellect. \n enter 3 to split. \n enter 4 to combine.')
    wtl = int(input("enter your choice: "))
    if wtl == 1:
        lst=List()
    elif wtl == 2:
        lst=Sel_List(lst)
    elif wtl == 3:
        lst=Slicing_List(lst)
##        elif wtl == 4:
##            lst=Combine_list(lst)
##            
    else:
        print('error')
    Using = input('enter yes to add, remove, or combine the items form the list: ')



 
#1
##Numbers = [1,2,3,4,5,6,7,8,9,10,11]
##print(len(Numbers))

#2 
#employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy','Robert']
#print(employees[4])


#3
#print(employees[1])

#4
#print(employees[5:7])

#5
##shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice','cereal']
##print(shopping_list[-1])
##
###6
##print(shopping_list[0:4])
##
###7
##print(shopping_list[2:5])

#8
##votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
##'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
##num_1 = votes.count('Jake')
##print(num_1)

#9
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
#10
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games.sort
print(games)
