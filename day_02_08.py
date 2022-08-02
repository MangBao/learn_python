
# random
import random

print(random.randrange(1, 10))

# dict
x = {"name" : "John", "age" : 36}

print (x["name"])

txt = "The best things in life are free!"
# print("free" in txt)

# split string
a = "Hello, World!"
b = a.split(",")
print(b)

# center string
txt = " banana "
x = txt.center(20, "*")
print(x)

# %d
age = 36
txt = "My name is John, and I am %d" % age
print(txt)

#  cast
_num = int(10.9785)
print(_num)

# extend
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
listname = ["long", "bao", "trong"]


thislist.extend(thistuple)
thislist.extend(listname)

print(thislist) 

# list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")

# print(thislist)

del thislist[1]
print(thislist)

# print list
def printList():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
        print(li)        
    
printList()

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


a = 6 
print('chẵn') if a % 2 == 0 else print('lẻ')

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

def my_function(*kids):
    print("The youngest child is " + kids[2])

# my_function(childv = "Emil", "Tobias", "Linus")