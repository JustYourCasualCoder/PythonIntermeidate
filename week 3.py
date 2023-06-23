##def string_char(a):
##    index = int(input("index of the Character? "))
##    print(a[index])
##
##
##def string_cut(a):
##    index = int(input("1st index: "))
##    value = int(input("2nd index: "))
##    sliced = a[index:value]
##    print(sliced)
##        
##def string_combine():
##    a = input("string 1: ")
##    b = input("string 2: ")
##    full_string = a+b
##    print(full_string)
##
##def string_char_num(a):
##    print(len(a))
##
##
##    
###main code
##a = input('input your string: ')
##Using = 'yes'
##while Using == 'yes':
##    print('enter 1 for a index in string. \n enter 2 to cut a string. \n enter 3 to combine strings. \n enter 4 to find #of char in a string.')
##    wtl = int(input("enter what type of string u need: "))
##    if wtl == 1:
##        string_char(a)
##    elif wtl == 2:
##        string_cut(a)
##    elif wtl == 3:
##        string_combine()
##    elif wtl == 4:
##        string_char_num(a)
##        
##    else:
##        print('error')
##    Using = input('enter yes repeat the entire thing again: ')


###1
##my_name = 'Dhairya'
##frist_initial =(my_name[0])
##print(frist_initial)
##
###2
##first_name = "Rodrigo"
##last_name = "Villanueva"
##
##new_account = last_name[0:5]
##print(new_account)
##
###3
##first_name = "Rodrigo"
##last_name = "Villanueva"
##temp_password = last_name[3:6]
##print(temp_password)
##
###4
##dessert_prefix = "Chocolate"
##dessert_suffix = "muffin"
##fav_food = dessert_prefix + dessert_suffix
##print(fav_food)

#5
#a
company_motto = "Ensuring every child has the opportunity to learn computer science"
second_to_last = company_motto[-2]
print(second_to_last)

#b
final_word = company_motto[-4:-1]
print(final_word)

#6
vari_password = "\theycallme\"crazy\"91")
print(vari_password)

