##fd_list = ["milk","eggs",'bread']
##print (fd_list)
##print(fd_list[0])
##print(fd_list[1])
##print(fd_list[2])


def List():
    lst = []
    Using = 'yes'
    while Using.lower() == 'yes':
        temp = input("enter list item: ")
        lst.append(temp)
        Using = input("Enter yes to continue: ")
    print(lst)
    return lst

def rem_list():
    Using = 'yes'
    while Using.lower() == 'yes':
        Rg = input("Do you want to remove a grade? ")
        if Rg.lower() == 'yes':
            Nol = input("name or location: ")
            if Nol == 'location':
                Dg = int(input("what grade do you want to remove? "))
                grades.pop(Dg)
                print(grades)
            elif Nol == 'name':
                Dg = input("what grade do you want to remove? ")
                grades.remove(Dg)
                print(grades)
            
        Using = input("Enter yes to remove another item: ")

def add_list():
    Using = 'yes'
    while Using.lower() == 'yes':
        index = int(input("where to put your item? "))
        value = input("name of item you want to add? ")
        grades.insert(index,value)
        print(grades)
    Using = input("Enter yes to add another item: ")

grades=List()
add_list()

wtl = input("what type of list? normal, removing or adding? ")
grades=List()
rem_list()
if wtl == 'nomral':
    List()
elif wtl == 'removing':
    rem_list()
elif wtl == 'adding':
    add_list()

##grades1=List()
##final_gra = grades+grades1
####grades.append(99)
####print(grades)
##print(final_gra)
##grades = [97,62,85,93]+[90,77]



