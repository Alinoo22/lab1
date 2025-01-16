#1
#PYTHON HOME
print ("Hello,world!") #Hello,world!


#2
#PYTHON INTRO
"""
What is Python?
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.

"""
print ("Hello,world!")

#3
#PYTHON GET STARTED
import sys

print(sys.version) #3.8.2 (default, Mar 13 2020, 10:14:16)
#[GCC 9.3.0]  


#4
#PYTHON SYNTAX
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
        #answer:Five is greater than two
            #   Five is greater than two
#Python will give you an error if you skip the indentation
        


#5
#PYTHON COMMENTS
        
print("Hello, world!") #This is a comment
#multiline comment
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



#6
#PYTHON VARIABLES
x = 5
y = "John"
print(x)
print(y) #answer: 5
          #       John


#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#get the type
x = 5
y = "John"
print(type(x))
print(type(y)) #answer:<class 'int'>
#                      <class 'str'>
#case-sensetive
a = 4
A = "Sally"
#A will not overwrite a      #answer: 4
#                                     Sally


#7
#PYTHON VARIABLE-NAMES
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" #answer:John
#                       John
#                       John
#                       John
#                       John
#                       John


#8
#PYTHON VALUES TO MULTIPLE VARIABLES
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)  #answer: 
 #                 apple  
 #                 banana
 #                 cherry



#9
#PYTHON - OUTPUT VARIABLES
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #answer: Python is awesome


#10
#PYTHON - GLOBAL VARIABLES
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  #answer: Python is awesome


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #answer:Python is fantastic




#11
#PYTHON DATA TYPES
#range
x = complex(1j)

#display x:
print(x)

#display the data type of x:
print(type(x))  #answer: 1j
#                        <class 'complex'>
#list
x = list(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x))            #answer:['apple', 'banana', 'cherry']
#                                 <class 'list'>
#bool
x = bool(5)

#display x:
print(x)

#display the data type of x:
print(type(x))            #answer: True
#                                  <class 'bool'>



#12
#PYTHON NUMBERS
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) #answer:<class 'float'>
#                      <class 'float'>
#                      <class 'float'>
#random
import random

print(random.randrange(1, 10)) #answer: 9


#13
#PYTHON CASTING
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2  #answer:1.0
#                                         2.8
#                                         3.0
#                                         4.2



#14
#PYTHON STRINGS
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')   #answer:It's alright
#                                        He is called 'Johnny'
#                                        He is called "Johnny"
#string length
a = "Hello, World!"
print(len(a))       #answer:13
#string array
a = "Hello, World!"
print(a[1])        #answer: e
#check string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")   #answer: Yes, 'free' is present.


#15
#PYTHON - SLICING STRINGS
a = " hello, world! "
print(a[3:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])


#16
#PYTHON - MODIFY STRINGS
#upper case
a = "Hello, World!"
print(a.upper()) #answer:HELLO, WORLD!
#lower case
a = "Hello, World!"
print(a.lower()) #answer:hello, world!
#remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  #answer:Hello, World!
#replace string
a = "Hello, World!"
print(a.replace("H", "J"))  #answer:Jello, World!
#split string
a = "Hello, World!" 
print(a.split(",")) # returns ['Hello', ' World!']  #answer:['Hello', ' World!']




#17
#PYTHON - STRING CONCATENATION
a = "Hello"
b = "World"
c = a + b 
print(c)  #answer:HelloWorld


#18
#PYTHON - FORMAT - STRINGS
age = 36
txt = f"My name is John, I am {age}"
print(txt)      #answer:My name is John, I am 36


#19
#PYTHON - ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north."
#answer:We are the so-called "Vikings" from the north.

