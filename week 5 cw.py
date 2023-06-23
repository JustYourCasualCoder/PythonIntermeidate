import datetime

#2
x = datetime.date.today()
print(x)

#3
x1 = datetime.datetime.now()
print(x1)

import random

#4
y = random.randint(0,100)
print(y)

#5
lst = ['Fight Back','Cold','Grateful','Death Motto', 'Destiny', 'Nowhere To Run', 'fearless', 'No Glory','Im good (blue)', 'Glory']
y2 = random.choice(lst)
print(y2)

#6
random.shuffle(lst)
print(lst)

#7
import webbrowser

webbrowser.open('https://www.ultimatecoders.ca/')

#8
webbrowser.open('https://www.youtube.com/')
