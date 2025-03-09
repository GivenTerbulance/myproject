
## Functions####
name = str(input("Enter your name:"))
def myfunc():
    print("Hello ", name)

name = name.capitalize()
if name == "Given":
 myfunc()

 ###Body_Mass_Index_Function### 
 ### Shipping_Cost###
# Calculating the shipping cost for customer orders based on weight of the Packages 
#Cost per kilogram is $5
weight= int(input("Measured weight:"))
def shipping_cost(weight):
   price = weight * 5
   print(price)

shipping_cost(weight)
  
def rect(length, width):
    area = length * width
    parameter = 2 * length + 2 * width
    return area, parameter

x,y = rect(3, 4)
print(x, y)
 
def nam(name = str(input("Enter Name:"))):
    print("Hello", name)
    
nam()
nam("Sebonelo")

###Menu Ta'Gives###
Starter = ["Risotto balls", "Mexican bread balls", "Chinese steamed dumbling"]
Food_items = ["Pizza", "Burger", "Pasta"]
drink_item = ["Water", "Soda_water", "Lemonade"]
desert = ["Fruits", "Custards", "Cakes"]

w = int(input("Choose Starter:"))
x = int(input("Choose Food_items:"))
y = int(input("Choose drink_item:"))
z = int(input("Choose desert:"))

def your_order(w,x,y,z):
    print("WELCOME TO TA'GIVES RESTURANT\n")
    diplay = w + z + x + y 
    return diplay

your_order(w, x, y, z)
print("You ordered: \n","Starter: \n", Starter[w], "\n", "Food_items: \n", Food_items[x], "\n", 
      "drink_items: \n", drink_item[y], "\n", "desert: \n", desert[z] )

### Cocatination and Capitalization
names = str(input("Enter the name:"))
def name(names):
    display = names + " " + "Watson"
    return display

concatination = name(names.capitalize())
print(concatination)

score = 80
def my_function(score):
    if score >= 70:
        return False

print(my_function(score))

#Smart_Library#
#The program is the assistant, that helps with searching the book in demand and telling where to find the book
##Adding a book to the shelf, for the administrator####
Books = ["Good Vibes, Author: Vex King, Publish: 4 December 2018",
         "The compound effect, Author: Darren hardy, Publish: 2010 ", 
         "Talk like TED, Author: Carmine Gallo, Publish: 4 March 2014 ", 
         "The Art of thinking Clearly, Author: Rolf Dobelli,Publish: 2011",
         "The power of your subconcious mind, Author: Joseph Murphy, Publish: 1963"]
sec_user = "Given"
sec_pass = "12345678"
print("Adding a book ?................")
answer = str(input("Are you....?: Y/N"))
if answer == "Y":
      print("For access enter your user_name and password: ")
      user_name = str(input("Enter the username:"))
      user_name = user_name.capitalize()
      password = int(input("Enter the password:"))
      if user_name == sec_user or sec_pass == password:
            book_name = str(input("Enter the book name:"))
            Books.append(book_name)
            print("Loading............................!@!!!")
            print("Book Successfully added")
            my_list = str(Books)
            print(my_list)
      else:
            print("Access denied!!!!!!!!!") 
            
else:
######################################################################
 print("The format to search for the book is: Book_name, Author,Publish")
 book = str(input("Enter the name of the book:"))

 def book_check(book):
     book_index = Books.index(book)
     if book in Books:
            print("Book is available")
            print("The book is found on shelf number: \n", book_index)
     else:
            print("Sorry the book is not available")

 book_check(book)
###############################SETS#########################################
name = str(input("Enter the name:"))

names = {"Given", "Bongi"}
names2 = {"Elias", "Wamaanda"}
name = name.capitalize()
names.add(name)
concatination = names.union(names2)
print(names)
print(concatination)
#Clear(), add(), remove(), union(), difference() are for sets {}
names.clear()
print(names)

set1 = {"Given", "Sipho","Neo"}
set2 = {"Given", "Sipho","Neo", "Karabo"}
unique = set1.difference(set2)
print("What is different on set2 compared to set2:", unique)
###############################Dictioneries#########################################

contact = {
    "name" : "John",
    "Company": "RC"
}

info_keys = contact.keys()
info_values = contact.values() 
info = contact.get("Company")
print(info_keys)
print(info_values)
print(info)

contact.update({"Company": "Eskom"})
print(contact["Company"])

nums = []
for x in range(1, 14):
    nums.append(x)
print(nums)

coordinates = (4, 7, 9)
coordinates[1] = 5
print(coordinates)

###Error handling and exceptons
try:
 price = [250, 300, 234, 400]
 total = sum(price)
 print(total)

except TypeError:
 print("Hello world")

#####################
colors = ['Red', 'Yellow', 'Green']
try:
  print(colors[10])
except IndexError:
  print("Out of range")
except NameError:
  print("Variable is not defined")

print("Happy shopping")

try:
  print(len(5))
except NameError:
  print("Variable is not defined")
except TypeError:
  print("Not iterable")

price = input()
try:
  price_value = int(price)
except ValueError:
  print("Please enter a number")

##My_project 

name = int(input("Enter the name:"))
try:
    print("Hello", name)
except TypeError:
 print("Your input must be a string")

##Given Project##
#PRACTICE EXERCISE
#Imagine you're programming a vending machine interface. The machine displays a list of products, and the user selects a product by entering its position in the list. 
# To ensure the machine operates smoothly, 
# it should handle cases where users input invalid positions without crashing.
#Task
#The program below displays a list of products available in a vending machine and asks the user to select a product by entering its index. 
# Complete the program so it either shows the selected product or prints wrong index if the entered index is out of range 
###

products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

# Write a try-except block to display the selected product
try:
    print(products[choice_index])
# or print "wrong index" if the input index is out of range
except IndexError:
    print("wrong index")
###finally###
try:
  print(len(3745))
except:
  print("Error")
finally:
  print("Save")
##else###
products = ['ball', 'toy', 'paper']
try:
  count = len(products)
except:
 print("Error")
else:
  print("Count of products:", count)
  

########################################################################################
###Functional Programming###

name = str(input("Enter your name:"))
def welcome(name):
  return "Welcome"+ " " + name
greet = welcome 

print(greet(name))

def welcome(name):    # defining the function 
  return "Welcome, " + name #returning the conc of str 

def process_user(name, func): #
    return func(name)

print(process_user("Given", welcome))

name = str(input("Enter name:"))
def input_name(name):
  return name + " "+ " Given"

def second_name(name, name2):
  return name2(name)

print(second_name(name, input_name))

# Taking a number and doubling it

num = int(input("Enter a number:"))

def operation(num):
  return "Number doubled is" + " " + str(num * 2)

def process(num, func):
  return func(num)

print(process(num, operation))

##Lambda function 

greet = lambda name: "Welcome, " +" "+ name
print(greet("Ediod"))
#OR
def greet(name):
  return "Welcome," + " "+  name

print(greet("Given"))


name = str(input("Enter name:"))
surname = str(input("Enter your surname:"))

concatination =(lambda name, surname: name + " "+ surname) (name, surname) 
print(concatination)

#maping#map(<function><iterable>)
#List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]

# Function to capitalize each name
def capitalize(name):
  return name.capitalize()

# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)

names = ["Justine", "Given", "Lesedi", "Sammy"]
surname  = "Ikaneng"
def surname_con(surname):
  return names + surname

concatination = list(map(names, surname_con))
print(concatination)
"""
#FILTER#
"""
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)

marks = [63, 46, 93, 49, 51, 87]

passed = filter(lambda mark: mark < 60, marks)

user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
new_list = list(filter(lambda : "" == True, user_answers))
print(new_list)
# using filter with a lambda expression


# Display the cleaned list of answers

class Car:
 def __init__(self, brand, model):
  self.brand = brand
  self.model = model

my_car = Car("Audi", "Polo")
print(my_car)

###Second class##

class Person:
  def __init__(self, gender, age):
    self.gender = gender
    self.age = age 

whoamI = Person(str(input("Enter your name:")), int(input("Enter your age:")))
print(whoamI.gender)
print(whoamI.age)

##Third class##

class Animals:
  

  def __init__(self, animal1, animal2):
     
    self.animal1 = animal1
    self.annimal2 = animal2

animal1 = str(input("Animal1:"))
animal2 = str(input("Animal2:"))
my_animals = Animals(animal1, animal2)
print("Animal1 is:" +" "+ my_animals.animal1)
print("Animal2 is :" +" "+my_animals.annimal2)
#Inheritance#
#Inheritance is a key of concept whereby we have an existing class with set of characteristics and
#behaviours, and these characteristics and behaviours can be passed to a new class
    
class Animal:
  def __init__(self, animal1):
    self.animal1 = animal1

  def move(self):
    print("Hoof")

my_dog = Animal("Fluffy")

print(my_dog.animal1)
my_dog.move()
 
##Surname_Inheritance_Project##

name = str(input("Enter your name :"))
surname1 = str(input("Enter your surname :"))
class Surname:
  def __init__(self, surname1):
    self.surname1 = surname1
  
  def concatination(self):
    print("The full names of the new born are:", surname1 + " "+name)

your_name = Surname(surname1) 
your_name.concatination()
##Adding the attributes to the child class

#parent class
class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax", "Bulldog", 5)
#inherited attribute
print(my_dog.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)

#Class_Inheritance

class legacy:
  def __init__(self, car):
    self.car =  car 

  def seats(self):
    print("you inherit a car with black seats")

my_car = legacy("BMW")
print(my_car.car)  
my_car.seats()

#class_child can have attributes without inheriting them
#from the parents 

class Names: 
  def __init__(self, firstborn):
    self.firstborn = firstborn

    def surname(self):
      print("Surname is Kutoane:")

class nicknames(Names):
  def __init__(self, firstborn,secondborn, thirdborn):
    super().__init__(firstborn)
    self.secondborn = secondborn
    self.thirdborn = thirdborn
  def come(self):
    print("Call you")

my_name = nicknames("Thiza", "Sthape", "KB")
print(my_name.firstborn)

print(my_name.secondborn)
print(my_name.thirdborn)
    
#Task_Ebook

class Book:
  def __init__(self, title,author):
    self.title = title
    self.author = author
 
class Ebook(Book):
  def __init__(self, title, author, file_size):
    super().__init__(title, author)
    self.file_size = file_size

my_ebook = Ebook("1984", "George Orwell", 10)
print(my_ebook.title)
print(my_ebook.author)
print(my_ebook.file_size, 'MB')

class Car:
  def __init__(self, model, year, color):
    self.model = model
    self.year = year
    self.__color = color

  def first(self):
    print(self.model, self.year)
  
  def second(self):
    print(self.__color)
   
my_car = Car("Audi", 2025, "Blue")

my_car.first()
my_car.second()
#Data hiding & Encapsulation

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accesing using name mangling
print(my_car._Car__odometer)

#@classmethod
title = str(input("Enter title:"))
author = str(input("Enter the author:"))
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book(title, author)

# Using the instance method to describe the book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)


