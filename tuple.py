thistuple = (1, "banana", "cherry", "orange", "kiwi", "melon", "mango")
thisarray = ["bao", "long", "trong"]

# access tuple items
appletring =  "Yes, {} is in the fruits tuple".format(thistuple[0])

if "apple" in thistuple:
    print(appletring)


# change tuple items
changevar = list(thistuple)
changevar[1] = "kiwi"
thistuple = tuple(changevar)

# tuple add item
thistuple = thistuple + ("grape",)
print(thistuple)

# unpacking tuple
thistuple = ("apple", "banana", "cherry")
(a,b,c) = thistuple
print(a,b,c)

# print array
for i in thisarray:
    print(i)
    
# print(type(thistuple[0]))
