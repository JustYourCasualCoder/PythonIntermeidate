def List():
    lst = []
    Using = 'yes'
    while Using.lower() == 'yes':
        temp = input("enter list item: ")
        lst.append(temp)
        Using = input("Enter yes to continue: ")
    print(lst)
    return lst

def Joinlist(lst):
    use=lst
    sep = input('enter separator: ')
    print(sep.join(use))

def Split_list(lst):
    re = lst
    val = input('enter what you want to use to split the list: ')
    print(re.split(val))





##fun = lst
##1 = input("what word do you want to replace? ")
##2 = input('what do you want to replace it with? ')
##print(fun.replace(1, 2))

ui = List()
Split_list(ui)
