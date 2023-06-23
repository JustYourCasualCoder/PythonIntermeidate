def List():
    lst = []
    Using = 'yes'
    while Using.lower() == 'yes':
        temp = input("enter list item: ")
        lst.append(temp)
        Using = input("Enter yes to continue: ")
    print(lst)
    return lst


def addlist(lst):
    Using = 'yes'
    while Using.lower() == 'yes':
        index = int(input("where to put your item? "))
        value = input("name of item you want to add? ")
        lst.insert(index,value)
        print(lst)
        Using = input("Enter yes to add another item: ")
    return lst

def rem_list(lst):
    Using = 'yes'
    while Using.lower() == 'yes':
        Rg = input("Do you want to remove a item? ")
        if Rg.lower() == 'yes':
            Nol = input("name or location: ")
            if Nol == 'location':
                Dg = int(input("what is the index value item that you want to remove? "))
                lst.pop(Dg)
                print(lst)
            elif Nol == 'name':
                Dg = input("what is the name of the item that you want to remove? ")
                lst.remove(Dg)
                print(lst)
        Using = input("Enter yes to remove another item: ")
    return lst


def Combine_list(lst):
    Using = 'yes'
    while Using.lower() == 'yes':
        List_1 = lst
        print('new list to glue with exsisting list')
        lst2 = List()
        lst_m = List_1 + lst2
        print(lst_m)
        Using = input('enter yes to add more: ')
    return lst

def Joinlist(lst):
    use=lst
    sep = input('enter separator: ')
    print(sep.join(use))


lst =[]
Using = 'yes'
while Using == 'yes':
    print('enter 1 to create. \n enter 2 to remove. \n enter 3 to add. \n enter 4 to combine. \n enter 5 to use a separator')
    wtl = int(input("enter your choice: "))
    if wtl == 1:
        lst=List()
    elif wtl == 2:
        lst=rem_list(lst)
    elif wtl == 3:
        lst=addlist(lst)
    elif wtl == 4:
        lst=Combine_list(lst)
    elif wtl == 5:
        Joinlist(lst)
        
    else:
        print('error')
    Using = input('enter yes to add, remove, or combine the items form the list: ')



