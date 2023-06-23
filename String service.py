def replace_str(string):
    string = string
    s1 = input("what word do you want to replace? ")
    s2 = input('what do you want to replace it with? ')
    print(string.replace(s1, s2))

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
    
#main
use = 'yes'
while use == 'yes':
    string = input('enter string: ')
    print(string)
    print(' enter 1 for upper. \n 2 for lower. \n 3 to replace a word. \n 4 to make it a title. \n 5 to split string. \n 6 to join string \n 7 to strip string')
    choice = int(input( 'enter your choice: '))
    if choice == 1:
        print(string.upper())
        use =input('enter yes to continue: ')
    elif choice == 2:
        print(string.lower())
        use =input('enter yes to continue: ')
    elif choice == 3:
        replace_str(string)
        use =input('enter yes to continue: ')
    elif choice == 4:
        print(string.title())
    elif choice == 5:
        s1 = input('enter what you want to split it with: ')
        lst=string.split(s1)
        print(lst)
        use =input('enter yes to continue: ')
    elif choice == 6:
        ui = int(input('enter 1 to use exsisting list, enter 2 to make a new list: '))
        if ui == 1:
            scp = input('new separator: ')
            print(scp.join(lst))
        elif ui == 2:
            new_lst = List()
            Jl=Joinlist(new_lst)
        use =input('enter yes to continue: ')

    elif choice == 7:
        Rem = input('input what u wanna strip form the string: ')
        print(string.strip(Rem))
        use =input('enter yes to continue: ')

    else:
        print('invailded input.')
        choice = int(input('enter your choice; (1-7)'))

