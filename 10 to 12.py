#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Basic of Python 
print("hello")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


#indentation 
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    #Exercise
#Use the "print" command to print the line "Hello, World!".


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[11]:


#Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare their type.
# Every variable in Python is an object.
    
#Numbers
#ython supports two types of numbers - integers and floating point numbers.

myinnt = 7
print(myint)
print(type(myinnt))


# In[15]:


myint = 7.1
print(myint)
print(type(myint))

#myfloat = float(7)
#print(myfloat)


# In[19]:


#Strings
#Strings are defined either with a single quote or a double quotes.

mystring = "let's see"
print(mystring)
print(type(mystring))


#mystring = "hello"
#print(mystring) 

#mystring = "hello"
#myfloat = 10.0
#myint = 20


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


#input from user

a = 10
b = 20
c = a + b
print(c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[28]:


#Lists
#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.
#Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

mylist = [2,4,5,6]
mylist.append(10)
print(mylist)
print(type(mylist))


# In[27]:


mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
#print(mylist)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[30]:


# prints out 1,2,3
for x in mylist:
    print(x)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


#Arithmetic Operators
#Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

number = 9.0343545
print("name is %f" % number)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


remainder = 11 % 3
print("remainder is %d " % remainder)


# In[46]:


squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


# In[47]:


lotofnames = "shekhar" * 10
print(lotofnames)


# In[48]:


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[70]:


#BAsic String Operations 

string = "Helloworld!"
string2 = 'Hello world!'

print(len(string))


# In[ ]:





# In[ ]:





# In[53]:


print(string.index("H"))


# In[55]:


print(string.count("l"))


# In[56]:


print(string[3:7])


# In[62]:


print(string[3:7:4])


# In[63]:


print(string.upper())


# In[64]:


print(string.lower())


# In[71]:


afewwords = string.split(" ")
print(afewwords)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[75]:


#Conditions
#Python uses boolean variables to evaluate conditions.
# The boolean values True and False are returned when an expression is compared or evaluated. For example:

x = 3

print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


# In[76]:


name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:


#Functions are a convenient way to divide your code into useful blocks,
# allowing us to order our code, make it more readable, reuse it and save some time.
# Also functions are a key way to define interfaces so programmers can share their code.

#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
# For example:



def sum_two_numbers(a, b):
    return a + b
x=  sum_two_numbers(5,6)
print(x)


#def shekhar():
 #   print("my name is shekhar")
    
#shekhar()


# In[81]:


def myname():
    print("hello i am shekhar")


def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

myname()
# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("Chandrashekhar", "a great year!")
# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

print(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[83]:


#Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.

class MyClass:
    variable = "welcome"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()


print(myobjectx.variable)
        #function()
myobjectx.function()



# In[84]:


#You can create multiple different objects that are of the same class(have the same variables and functions defined).
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

#myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

#Exercise
#We have a class defined for vehicles. Create two new vehicles called car1 and car2.
#Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.


# In[87]:


#loops 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In[88]:


#break 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
          break
    print(x)


# In[89]:


#Continue

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
           continue
    print(x)


# In[91]:


#range 

for x in range(10):
  print(x)


# In[94]:


for x in range(3, 33, 3):
      print(x)


# In[95]:


a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# In[96]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#SOUP

import requests
from bs4 import BeautifulSoup

url= "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "maincounter-number")

print("Total Cases :",data[0].text.strip())
print("Total Deaths:",data[1].text.strip())
print("Total Recoverd:",data[2].text.strip())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[103]:


import requests
from bs4 import BeautifulSoup

search = "facebook "
url = f"https://www.google.com/search?&q={search}"

r= requests.get(url)

s= BeautifulSoup(r.text,"html.parser")

update = s.find("div",class_="BNeawe").text
print(update)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#ranom number game 
import random

number = random.randint(1, 10)
print(number)

print("guess a number (between 1 and 10):")

guess = int(input("enter your guess:"))

if guess == number:
    print("Congo you won")
    exit()

elif guess < number:
    print("your guess was too low")

else:
    print("your guess was too high")

print("you lose!!! The number is : ", number)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[104]:


#TQDM
from tqdm import tqdm
from time import sleep


for i in tqdm (range(100)):sleep(0.2)


# In[ ]:





# In[ ]:





# In[105]:


#encoding and Decoding
import base64

print("encode encode\n")
str=" i am shekhar"
s1=str.encode("ascii")
s2=base64.b64encode(s1);
print("encoed:",s2)
print("decoded:",base64.b64decode(s2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import requests
from bs4 import BeautifulSoup

URL = " https://www.instagram.com/{}/"

def scrape(username):
    full_url = URL.format(username)
    r = requests.get(full_url)
    s = BeautifulSoup(r.text,"lxml")

    tag = s.find("meta",attrs={"name":"description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text

USERNAME ="ashu_msa_3"
data = scrape(USERNAME)
print(data)


# In[97]:


conda install requests


# In[ ]:




