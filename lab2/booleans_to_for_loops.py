#1
#PYTHON BOOLEANS
#boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9) #answer:True
#                     True
#                     False
#Evaluate Values and Variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y)) #answer:True
#                      True
#Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})   #answer:False
#                  False
#                  False
#                  False
#                  False
#                  False
#                  False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #answer: False



#2
#PYTHON OPERATORS
# Arithmetic Operators
x = 5
y = 3

print(x + y)
#Assignment Operators
x = 5

x += 3

print(x)
#Comparison Operators
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3
#Logical Operators
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#Membership Operators
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
#print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#Operator Precedence
print((6 + 3) - (6 + 3))



#3
#PYTHON LISTS
#list
thislist = ["apple", "banana", "cherry"]
print(thislist)                          #answer:['apple', 'banana', 'cherry']
#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))     #answer:3
#Python - Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])         #answer:banana
#Python - Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)                    #answer:['apple', 'blackcurrant', 'cherry']



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)   #answer:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#Python - Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)     #answer:['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)    #answer:['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)    #answer:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Python - Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)      #answer:['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)   #answer:['apple', 'cherry', 'banana', 'kiwi']

#remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)   #answer:['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  #answer:[]

#Python - Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)     #answer:apple
#                      banana
#                      cherry
#Python - List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)    #answer:['apple', 'banana', 'mango']

#Python - Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)    #answer:['banana', 'kiwi', 'mango', 'orange', 'pineapple']
#Python - Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)   #answer:['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)   #answer:['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)    #answer:['apple', 'banana', 'cherry']

#Python - Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)    #answer:['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)    #answer:['a', 'b', 'c', 1, 2, 3]






#4
#PYTHON TUPLES
thistuple = ("apple", "banana", "cherry")
print(thistuple)  #answer:('apple', 'banana', 'cherry')
#Python - Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])         #answer:banana
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included      #answer:('cherry', 'orange', 'kiwi')
#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)   #answer:("apple", "kiwi", "cherry")
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) #answer:('apple', 'banana', 'cherry', 'orange')
#unpack tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)              #answer: apple banana cherry
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)          #answer:apple
#                           banana
#                           ['cherry', 'strawberry', 'raspberry']
#loop tuples
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1               #answer:apple
#                                 banana
#                                 cherry
#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)          #answer:('a', 'b', 'c', 1, 2, 3)









#5
#PYTHON SETS
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.  #answer:{'banana', 'apple', 'cherry'}
#access set items
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)    #answer:True
#Add set items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)           #answer:{'apple', 'orange', 'banana', 'cherry'}
#remove set items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)   #answer:{'cherry', 'apple'}
#loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)        #answer:banana
#                         cherry
#                         apple
#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)           #answer:{'c', John, 1, 'a', 'b', 2, 3, Elena, apple, banana, cherry}







#6
#PYTHON DICTIOANARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  #answer:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#access items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)      #answer:dict_keys(['brand', 'model', 'year'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)     #answer:dict_values(['Ford', 'Mustang', 1964])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)    #answer:dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#change items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 
print(thisdict)            #answer:{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
#add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})   #answer:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)        #answer:{'brand': 'Ford', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)          #answer:{'brand': 'Ford', 'model': 'Mustang'}
#loop dictioanaries
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)              #answer: brand model year
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])    #answer: Ford Mustang 1964
#copy dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)           #answer:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)         #answer:{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}








#7
#PYTHON IF... ELSE
a = 33
b = 200
if b > a:
  print("b is greater than a")    #answer:b is greater than a

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")     #answer:a and b are equal

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")   #answer:a is greater than b

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")   #answer:Above ten,
#                                        and also above 20!







#8
#PYTHON WHILE LOOPS
i = 1
while i < 6:
  print(i)
  i += 1    #answer:1 2 3 4 5

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)   #answer:1 2 4 5 6
 








#9
#PYTHON FOR LOOPS
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)       #answer:apple
#                        banana
#                        cherry
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break         #answer:apple
#                         banana
for x in range(2, 6):
  print(x)               #answer:2 3 4 5


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)    #answer:
#                         red apple
#                         red banana
#                         red cherry
#                         big apple
#                         big banana
#                         big cherry
#                         tasty apple
#                         tasty banana
#                         tasty cherry