import random
import datetime
import webbrowser

#1
lst = ['Fight Back','Cold','Grateful','Death Motto', 'Destiny', 'Nowhere To Run', 'fearless', 'No Glory','Im good (blue)', 'Glory']
random.shuffle(lst)
print(lst)

#2
a = random.random()
print(a)

#3

webbrowser.open('https://www.google.com/')

#4

x1 = datetime.date.today()
print(x1)


#5
y = random.randint(0,100)
print(y)

#6
y2 = random.choice(lst)
print(y2)

#7 
x2 = datetime.datetime.now()
print(x2)

#8
webbrowser.open('https://scratch.mit.edu/')
