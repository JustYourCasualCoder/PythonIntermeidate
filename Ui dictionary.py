def Dict():
    ed = {}
    Using = 'yes'
    while Using.lower() == 'yes':
        it = input("enter dictionary item: ")
        val = input("enter dictionary item Value: ")
        ed[it] = val
        Using = input("Enter yes to continue: ")
    print(ed)
    return ed


def Mul_key(ed):
    Using = 'yes'
    while Using.lower() == 'yes':
        it = (input("name of item you want to add? "))
        val = input("value? ")
        ed.update({it:val})
        print(ed)
        Using = input("Enter yes to add another item: ")
    return ed

def Ovr_wd(ed):
    Using = 'yes'
    while Using.lower() == 'yes':
        it = (input("name of item who's value you want to change? "))
        val = input("New value of item? ")
        ed[it] = val
        print(ed)
        Using = input("Enter yes to overwrite another item: ")
    return ed

def fd_key (ed):
    Using = 'yes'
    while Using.lower() == 'yes':
        it = (input("name of item you want to find? "))
        print(ed.get(it))
        Using = input("Enter yes to find another item: ")

def del_key(ed):
    Using = 'yes'
    while Using.lower() == 'yes':
        val = int(input("key? "))
        it = (input("default value to return if the key does not exist: "))
        print(ed.pop(val,it))
        Using = input("Enter yes to find another item: ")    

def all_key(ed):
    for it in ed.keys():
        print(it)

def all_val(ed):
    for re in ed.values():
        print(re)



lst =[]
Using = 'yes'
while Using == 'yes':
    print('enter 1 to create. \n enter 2 to update. \n enter 3 to overwrite value')
    wtl = int(input("enter your choice: "))
    if wtl == 1:
        ed = Dict()
    elif wtl == 2:
        ed= Mul_key(ed)
    elif wtl == 3:
        ed = Ovr_wd(ed)
    elif wtl == 4:
         ed = fd_key(ed)
    elif wtl == 5:
         ed= del_key(ed)
    elif wtl == 6:
         ed =  all_key(ed)
    elif wtl == 7:
         ed = all_val(ed)
        
    else:
        print('error')
    Using = input('enter yes to create, update, or overwrite value of items form the dictionary: ')




























































##    elif wtl == 4:
##         ed= (ed)
##    elif wtl == 5:
##         ed= (ed)
    
#def rem_list(lst):
##    Using = 'yes'
##    while Using.lower() == 'yes':
##        Rg = input("Do you want to remove a item? ")
##        if Rg.lower() == 'yes':
##            Nol = input("name or location: ")
##            if Nol == 'location':
##                Dg = int(input("what is the index value item that you want to remove? "))
##                lst.pop(Dg)
##                print(lst)
##            elif Nol == 'name':
##                Dg = input("what is the name of the item that you want to remove? ")
##                lst.remove(Dg)
##                print(lst)
##        Using = input("Enter yes to remove another item: ")
##    return lst
##
##
##def Combine_list(lst):
##    Using = 'yes'
##    while Using.lower() == 'yes':
##        List_1 = lst
##        print('new list to glue with exsisting list')
##        lst2 = List()
##        lst_m = List_1 + lst2
##        print(lst_m)
##        Using = input('enter yes to add more: ')
##    return lst
##
##def Joinlist(lst):
##    use=lst
##    sep = input('enter separator: ')
##    print(sep.join(use))
    


