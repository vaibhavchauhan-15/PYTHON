# Day 1: User Input and Basic Arithmetic Operations               
a = input("Enter your name: ")  # Taking user input for name            
print("Your name is:", a)  # Printing the entered name        

x = int(input("Enter first number: "))  # Taking first number as input
y = int(input("Enter second number: "))  # Taking second number as input  
 
print("Addition:", x + y)  # Performing addition
print("Subtraction:", x - y)  # Performing subtraction
print("Division:", x / y)  # Performing division
print("Multiplication:", x * y)  # Performing multiplication
print("Remainder:", x % y)  # Calculating remainder

# Day 11: Looping Through a String
andry = 'vaibhav'  # Defining a string
for character in andry:  # Looping through each character in the string
    print(character)  # Printing each character

# Day 12: String Slicing and Indexing
names = "ankit ka bacchi"  # Defining a string
print(names[0:9])  # Printing characters from index 0 to 8
print(len(names))  # Printing the length of the string
print(names[0:15:2])  # Printing every second character from index 0 to 14
print(names[:])  # Printing the entire string
print(names[2:10])  # Printing characters from index 2 to 9
print(names[3:-1])  # Printing characters from index 3 to second last character
print(names[-5:-2])  # Printing characters using negative indexing
print(names[0:-6])  # Printing characters from index 0 to -6

# Day 13: String Methods
str = "Vaibhav"  # Defining a string
print(str.upper())  # Converting to uppercase
print(str.lower())  # Converting to lowercase
print(str.rstrip('v'))  # Removing trailing 'v'
print(str.lstrip('V'))  # Removing leading 'V'
print(str.replace('Vaibhav', 'Khushi'))  # Replacing 'Vaibhav' with 'Khushi'
print(str.split("b"))  # Splitting the string at 'b'

str1 = "vaibhav chauhan"  # Defining another string
print(str1.capitalize())  # Capitalizing the first letter
print(str1.title())  # Capitalizing the first letter of each word
print(len(str1))  # Printing the length of the string
print(len(str1.center(50)))  # Centering the string and printing its length
print(str1.count("vaibhav"))  # Counting occurrences of 'vaibhav'
print(str1.startswith("V"))  # Checking if the string starts with 'V'
print(str1.endswith("v"))  # Checking if the string ends with 'v'
print(str1.endswith("a", 1, 5))  # Checking if it ends with 'a' within a range
print(str1.find("ai"))  # Finding the position of 'ai'
print(str1.index("ai"))  # Finding the index of 'ai'

str = " hlo ji kya hal chal"  # Defining another string
str2 = "     "  # Defining a string with spaces
print(str.isalnum())  # Checking if the string is alphanumeric
print(str.isalpha())  # Checking if the string is alphabetic
print(str.islower())  # Checking if the string is in lowercase
print(str.isupper())  # Checking if the string is in uppercase
print(str.isprintable())  # Checking if the string is printable
print(str2.isspace())  # Checking if the string contains only spaces
print(str.istitle())  # Checking if the string is in title case
print(str.swapcase())  # Swapping the case of each character

# Day 14: Conditional Statements
a = int(input("Enter your age: "))  # Taking age as input
if a >= 18 and a < 60:  # Checking if age is between 18 and 59
    print("You can vote. Please vote responsibly!")  # Printing a message for eligible voters
elif a >= 60:  # Checking if age is 60 or above
    print("You are a senior citizen. Take care and stay healthy!")  # Printing a message for senior citizens
else:  # If age is below 18
    print("You are too young to vote. Stay safe!")  # Printing a message for underage users



# Day 15: Time-based Greetings and Time Module
# Ask the user to input the hour in 24-hour format and print a corresponding greeting based on the time of day.
a = int(input("Enter the hour till 12 am in 24H format: "))
if a <= 12:
    print("GOOD MORNING BHAI JI!")
elif a > 12 and a <= 16:
    print("GOOD AFTERNOON BHAIYA JI!")
elif a > 16 and a < 20:
    print("GOOD EVENING BHAI JI!")
elif a >= 20 and a <= 24:
    print("GOOD NIGHT JI!")
else:
    print("Andhera kayam rahe!")

# Using the time module to get the current time in different formats.
import time
timestamp = time.strftime('%H:%M:%S')
print("Current Time:", timestamp)
timestamp = time.strftime('%H')
print("Current Hour:", timestamp)
timestamp = time.strftime('%M')
print("Current Minutes:", timestamp)
timestamp = time.strftime('%S')
print("Current Seconds:", timestamp)

# Day 16: Match Case Statement
# Create a menu using match-case statements for different time greetings.
print("Press 1 for Morning\nPress 2 for Afternoon\nPress 3 for Evening\nPress 4 for Night")
a = int(input("Enter your choice: "))
match a:
    case 1:
        print("GOOD MORNING")
    case 2:
        print("GOOD AFTERNOON")
    case 3:
        print("GOOD EVENING")
    case 4:
        print("GOOD NIGHT")
    case _:
        print("Bye Bye")

# Day 17: For Loop
# Print each character in a string using a for loop.
name = "Hariom Prashad Rajkumar"
for i in name:
    print(i, end=", ")

# Print each character without a separator.
name = "Vaibhav Chauhan"
for i in name:
    print(i)

# Using range function in for loops.
for num in range(10):
    print(num)
for num in range(10, 15):
    print(num)
for num in range(10, 20, 2):  # Step by 2
    print(num)

# Day 18: While Loop
# Print "hii" multiple times based on user input.
n = int(input("Enter a number of times you want to print: "))
a = 0
while a <= n:
    print("Hii")
    a += 1

# Countdown using while loop.
count = 5
while count > 0:
    print(count)
    count -= 1

# Day 19: Continue and Break in Loops
# Print a multiplication table for 5, skip 5 and break at 10.
for i in range(1, 11):
    if i == 5:
        continue
    print("5 X", i, "=", 5 * i)
    if i == 10:
        break

# Day 20: Functions
# Function to check which number is greater.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def is_greater(a, b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")

# Function to check which number is smaller.
def is_less(a, b):
    if a < b:
        print("a is smaller")
    else:
        print("b is smaller or equal")

# Function to calculate the average of two numbers.
def avg(a, b):
    c = (a + b) / 2
    print("The average value is:", c)

# Function to print the multiplication table of a number.
def table(a):
    for i in range(10):
        print(a, 'x', i + 1, '=', a * (i + 1))

is_greater(a, b)
is_less(a, b)
avg(a, b)
table(a)

# Day 21: Default Arguments in Functions
# Function with default arguments.
def avg(a=2, b=3):
    sum = (a + b) / 2
    print("Average is:", sum)

avg()
avg(5)
avg(5, 6)

# Function with default arguments to print a name.
def name_print(fname="Aman", mname="Kamal", lname="Kumar"):
    print("Hello!", fname, mname, lname)

name_print()
name_print("Komal")
name_print("Komal", "Ramji")
name_print("Sanjana", "Akhilesh", "Chauhan")

# Day 22: Lists
# Basic list operations.
a = [1, 2, 4, 5, 5, 2, 5, 7, 3, 7, 9, 7, 5, 4, 3, 3, 4]
name = ["Ram", "Mohan", "Kali", "Windows"]
print(a)
print(a[-1])
print(a[1:5])
print(a[1:8:2])
print(a[1:-1:2])
print(name)
print(name[1])
print(name[1:5])
print(name[1:8:2])

# Check if an element is in the list.
if "Ram" in name:
    print("Yes")

# Palindrome check.
value = input("Enter a value: ")
n = value[::-1]
if value == n:
    print("It is a palindrome")
else:
    print("Not a palindrome")

# Day 23: List Methods
l = [1, 5, 8, 6, 9, 5, 8, 5, 3, 8]
print(l)
l.append(7)
print(l, "after append")
l.sort()
print(l, "after sort")
l.sort(reverse=True)
print(l, "after reverse sort")
print(l.index(1))  # Print the index of 1
print(l.count(5))  # Count occurrences of 5

l.insert(3, 777)
print(l, "after insert 777")
m = [44, 665, 9656]
l.extend(m)
print(l, "after extend")

# Day 24: Tuples
# Basic tuple operations.
tup = (45, 87, 69, 57, 46, 32, 78)
print(type(tup), tup)
print(len(tup), "length of tuple")
print(tup[1])
print(tup[-1])
print(tup[5])
print(tup[:6])
tup2 = tup[:3]
print(tup2)

# Day 25: Tuple to List Conversion and Operations
tup = [45, 87, 32, 69, 57, 46, 32, 78]
country = ("India", "Japan", "UK", "Finland", "Saudi")
name = ("Ram", "Sita", "Lakshman", "Hanuman")

# Convert tuple to list for modification.
temp = list(country)
temp.append("Kuwait")
temp.pop(2)
temp[3] = "Baigan"
temp.extend(tup)
country = tuple(temp)
print(country)

final = country + name
print(final)

# Count occurrences and find the index of an element in the tuple.
temp2 = tup.count(45)
print(temp2)
temp3 = tup.index(32, 3, 8)
print(temp3)

# Day 26: Time-based Greetings Using Time Module
import time
t = time.strftime('%H:%M:%S')
print("Current Time:", t)
hour = int(input("Enter hour: "))
if hour >= 0 and hour < 12:
    print("GOOD MORNING SIR!")
elif hour >= 12 and hour < 16:
    print("GOOD AFTERNOON SIR!")
elif hour >= 16 and hour <= 19:
    print("GOOD EVENING SIR!")
elif hour > 19 and hour <= 24:
    print("GOOD NIGHT SIR!")

# Day 27: Exercise Placeholder
# Day 28: f-Strings and String Formatting
letter = "My name is {2} and \nI am from {1}\nI am {0} years old"
name = "Vaibhav Chauhan"
place = "Bihar"
age = 19
print(letter.format(age, place, name))
print(f"\n\nUSING F-STRING:\n\nMy name is {name} and \nI am from {place}\nI am {age} years old")

price = 84.034254
print(f"The price of dollar is: {price:.2f}")

# Day 29: Docstrings
# Function with a docstring to add two numbers.
def sum(a, b):
    '''Add two integers and return the sum.'''
    return a + b

print(sum(5, 4))
print(sum.__doc__)

# Day 30: Recursion
# Function to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 4:", factorial(4))

# Function to generate Fibonacci numbers using recursion.
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci number at position 5:", fibonacci(5))

# Day 31: Working with Sets

# Creating a set and removing duplicates
names = {"ram", "shyam", "jon", "ram", "jack", "shyam"}
print(names)

# Iterating over a set
for name in names:
    print(name)

# Creating different types of sets
empty_dict = {}
empty_set = set()
print(type(names))  # set
print(type(empty_dict))  # dict
print(type(empty_set))  # set

# Day 32: Set Methods

cities = {"vadodara", "thane", "surat", "kutch"}
state1 = {"gujarat", "bihar", "maharashtra", "assam", "kerala"}
state2 = {"jammu", "kashmir", "ladakh", "bihar", "assam", "gujarat"}
state3 = {"jammu", "kashmir"}

# Set operations
print("Difference:", state1.difference(state2))
print("Union:", state1.union(state2))
print("Intersection:", state1.intersection(state2))
print("Symmetric Difference:", state1.symmetric_difference(state2))

# Checking relationships between sets
print("Is disjoint:", state1.isdisjoint(cities))
print("Is superset:", state2.issuperset(state3))
print("Is subset:", state3.issubset(state2))

# Adding and removing elements
state3.add("har har mahadev")
print("After add:", state3)
state3.remove("har har mahadev")
print("After remove:", state3)
state3.pop()
print("After pop:", state3)
state3.clear()
print("After clear:", state3)

# Day 33: Working with Dictionaries

dictionary = {
    'name': 'vaibhav',
    'age': 19,
    'weight': 500
}

info = {
    1: 'student1 grade A',
    2: 'student2 grade A',
    3: 'student3 grade B'
}

# Accessing dictionary values
print(dictionary)
print(info)
print(info[2])
print(info.keys())
print(info.values())

for value in info.values():
    print(value)

# Day 34: Dictionary Methods

std1 = {600: 68, 297: 90, 65: 85, 75: 0}
std2 = {635: 64, 227: 50, 785: 55, 855: 707, 58: 55, 655: 20}

# Accessing and modifying dictionaries
print(std1)
print(std2)
print(std1[65])

std2.popitem()
print("After pop item:", std2)
std1.pop(65)
print("After pop:", std1)

std2.update(std1)
print("After update:", std2)
std2.clear()
print("After clear:", std2)

del std1[600]
print("After delete item:", std1)

# Day 35: For Loop with Else Statement

# Using for loop with else
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Else block")

# Using while loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Else block")

# Using while loop with break
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("Else block")

# Day 36: Exception Handling

try:
    num = int(input("Enter a number: "))
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError as e:
    print("Invalid input. Please enter a valid number.")

# Day 37: Finally Keyword

try:
    lst = [1, 2, 5, 3, 2, 6]
    idx = int(input("Enter the index number: "))
    print(lst[idx])
except IndexError as e:
    print("Index out of range.")
finally:
    print("Finally block executed.")

# Day 38: Custom Errors

try:
    num = int(input("Enter a number between 5 and 9: "))
    if num < 5 or num > 9:
        raise ValueError("Invalid input.")
except ValueError as e:
    print(e)

# Day 39: Kaun Banega Crorepati (KBC) Game

questions = [
    {"question": "Who is the first Prime Minister of India?", "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Indira Gandhi", "D) Sardar Patel"], "answer": "A"},
    {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"},
    {"question": "Who wrote 'Hamlet'?", "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"], "answer": "B"},
    {"question": "What is the boiling point of water?", "options": ["A) 90°C", "B) 100°C", "C) 120°C", "D) 80°C"], "answer": "B"}
]

def play_kbc():
    print("Welcome to Kaun Banega Crorepati!")
    prize_money = 0
    prize_levels = [1000, 5000, 10000, 50000, 100000]

    for idx, q in enumerate(questions):
        print(f"\nQuestion for ₹{prize_levels[idx]}:")
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("Correct answer!")
            prize_money = prize_levels[idx]
        else:
            print(f"Wrong answer! The correct answer was {q['answer']}.")
            break

    print(f"\nYou have won ₹{prize_money}. Thank you for playing!")

play_kbc()

# Day 40: Encryption and Decryption

import random
import string

def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        modified_word = word[1:] + first_letter
        random_prefix = ''.join(random.choices(string.ascii_letters, k=3))
        random_suffix = ''.join(random.choices(string.ascii_letters, k=3))
        return random_prefix + modified_word + random_suffix
    else:
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        stripped_word = word[3:-3]
        last_letter = stripped_word[-1]
        return last_letter + stripped_word[:-1]

def encode_message(message):
    words = message.split()
    return ' '.join(encode_word(word) for word in words)

def decode_message(message):
    words = message.split()
    return ' '.join(decode_word(word) for word in words)

# Example usage
original_message = input("Enter the message: ")
encoded_message = encode_message(original_message)
decoded_message = decode_message(encoded_message)

print("Original Message:", original_message)
print("Encoded Message:", encoded_message)
print("Decoded Message:", decoded_message)

# Day 41: Short Hand If-Else Statement
# Using short-hand if-else statement to compare two numbers
a = 5
b = 3
print("A") if a > b else print("=") if a < b else print("B")

# Using short-hand if-else statement to assign a value based on a condition
c = 9 if a > b else 10
print(c)

# Day 42: Enumerate Function
# Printing marks with index and adding a condition to print "awesome" when index is 6
marks = [12, 34, 64, 24, 26, 75, 96, 32, 65, 98, 57]
index = 0
for mark in marks:
    print(mark)
    if index == 6:
        print("awesome")
    index += 1

# Using enumerate function to achieve the same result
for index, mark in enumerate(marks):
    print(mark)
    if index == 6:
        print("awesome")

# Day 43: Virtual Environment
# (Virtual environment setup instructions would go here)

# Day 44: Import in Python
# Demonstrating different ways to import modules
import math as m
import pandas
print(m.sqrt(5) * m.pi)

# Importing a custom module
def daa():
    print("DAA function called")
daa()

# Day 45: if __name__ == "__main__"
import vaibhav
vaibhav.welcome()

# Day 46: OS Module in Python
# Demonstrating basic operations with the os module
import os
print(os.getcwd())

if not os.path.exists("oslist"):
    os.mkdir("oslist")

# Renaming a directory
os.rename("oslist/day1", "oslist/list1")

# Day 47: Exercise - Encryption and Decryption
coding = int(input("1 for encode and 0 for decode: "))
st = input("Enter your message: ")
words = st.split(" ")

coding = True if coding == 1 else False
newwords = []

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = "jhs"
            r2 = "dkf"
            newst = r1 + word[1:] + word[0] + r2
            newwords.append(newst)
        else:
            newwords.append(word[::-1])
else:
    for word in words:
        if len(word) >= 3:
            st = word[3:-3]
            st = word[-1] + word[:-1]
            newwords.append(st)
        else:
            newwords.append(word[::-1])

print(" ".join(newwords))

# Day 48: Local and Global Variables
x = 4
y = 9  # Global variable

print(f"Global variable x = {x}")

def fun():
    z = 5  # Local variable
    global x
    x = 10
    print(f"Local variable z = {z}")

fun()
print(f"Global variable y = {y}")
print(f"Global variable x = {x}")
# print(z)  # This will give an error because z is a local variable

# Day 49: File I/O in Python
try:
    f = open('hello.txt', 'r')
    seen = f.read()
    print(seen)
    f.close()
except FileNotFoundError:
    print("The file 'hello.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Day 50: File Methods - read(), readline(), readlines()
f = open('hello.txt', 'r')

# Reading file line by line
while True:
    line = f.readline()
    if not line:
        break
    print(line)
    print("\n")

# Reading all lines at once
lines = f.readlines()
print(lines)

# Writing multiple lines (this part is commented as it requires file handling permissions)
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
f.close()


#days 51 seek(),tell() and tuncate


f=open('myfile.txt','w')
f.write('hlo ji kya haal')
f.write('djfgkjagsal')
f.write('hljsdgkbghaal')
f.write('hsjhdfal')
f.write('hsjdhfvvgl')
f.write('hlo hal')
f.close()

with open('myfile.txt','r') as f:
    f.seek(6)#jump to the 7th letter
    print(f.read())

f=open('myfile.txt','w')
f.write('ksdglhjabs')
f.truncate(5)#after 5 letter all are deleted
f.close()

with open('myfile.txt','r') as f:
  print(f.readlines())

#days 52 lambda function(anonymous function)


def sum(fx,b):
    return fx + b
# a=6
# b=9
# c=sum(a,b)
# print(c)


a=3
b=8
rum=lambda a,b: a+b
result = rum(a,b)
print(sum(result,b))

#days 53 map , filter , reduce in python

def cube(x):
    return x*x*x
print(cube(2))


l = [3,5,6,2,8,9]
new=[]
for i in l:
    new.append(cube(i))
print(new)


#now using map
newlist=[]
newlist=list(map(cube,l))
print(newlist)


#now using filter

def filter_fun(a):
    return a>2
l = [3,5,6,2,8,9]
nl=list(filter(filter_fun ,l))
print(nl)

from functools import reduce
print("using reduce function")
l = [3,5,6,2,8,9]

newl=reduce(lambda a,b:a+b,l)
print(newl)


#days 54 "is" and "=="

a=5
b="5"
print("\nfirst block")
print(a is b) #it compare the address of the object/varible/value
print(a == b)#it compare the value


print("second block")
print(a is 5)
print(b is 5)

print("\nthird block")
print(b is "5")
print(a is "5")


print("\nforth block")
print(a==5)
print(b==5)

#days 55 snake water and gun game
import random
print("*********WELCOME TO THE SNAKE  WATER  GUN GAME***************\n")
comp= random.randint(0,2)
user=int(input("Enter your choice SNAKE(O),WATER(1),GUN(2):"))
if (comp==0):
    print("Coumputer choice: Snake")
if (comp==1):
    print("Coumputer choice: Water")
if(comp==2):
    print("Coumputer choice: Gun")

if (user==0):
    print("Your choice: Snake")
if (user==1):
    print("Your choice: Water")
if(user==2):
    print("Your choice: Gun")


if(user<=2 and user>=0 ):
    if comp == 0 and user == 0:
        print("Result: Draw!!!")
    if comp == 1 and user == 0:
        print("Result: Yayy!!! ^_^ you Won")
    if comp == 2 and user == 0:
        print("Result: Lose :(:(  Better Luck Next Time!!!")
    if comp == 0 and user == 1:
        print("Result: Lose :(:(  Better Luck Next Time!!!")
    if comp == 1 and user == 1:
        print("Result: Draw!!!")
    if comp == 2 and user == 1:
        print("Result: Yayy!! ^_^ you Won")
    if comp == 0 and user == 2:
        print("Result: Yayy!!! ^_^ you Won")
    if comp == 1 and user == 2:
        print("Result: Lose :(:(  Better Luck Next Time!!!")
    if comp == 2 and user == 2:
        print("Result: Draw!!!")
else:
    print("Enter valid choice!!!")


#days 56 OOps concept

#days 57 class and object

class student:
    name= "rohan"
    rollno=23
    department="cse"
    def info(self):
        print(f"student name is {self.name} and roll no is {self.rollno} from {self.department}")

obj=student()

print(obj.name)
obj.name="kalya"
print(obj.name)
obj.name="soham"
obj.info()


#days 58 constructor

class emp:
    def __init__(self,name,branch):
        print("i am cunstructor")
        self.name=name
        self.branch=branch

    def info(self):
        print(f"{self.name} working in {self.branch} department")

obj=emp("karan","cyber")
obj1=emp("arjun","design")

obj.name="arya"
obj.branch="cse"
obj.info()
obj1.info()


#days 59 python decorators

def greet(fx):
    def mfx():
        print("good morning ")
        fx()
        print("thank you for using me")
    return mfx

@greet
def hello():
    print("hello how are you")

def wish(fx):
    def mfx(*args,**kwargs):#list and tuple
        print("good morning ")
        fx(*args,**kwargs)
        print("thank you for using me")
    return mfx


# @wish
def add(a,b):
    c=a+b
    print(c)

hello()
# greet(hello)()
# add(1,3)
wish(add)(1,3)


#days 60 getter and setter

class myclass:
    def __init__(self,value):
        self.newvalue=value

    def Printing(self):
        print(f"original value is :{self.newvalue}")


    @property
    def ten_value(self):
        return print(f"multiple of ten :{10*self.newvalue}")

    @ten_value.setter
    def ten_value(self,new_value):
        self.newvalue=new_value /10

obj=myclass(10)
obj.Printing()
print(obj.ten_value)
obj.newvalue=9
print(obj.ten_value)
obj.Printing()


#days 61 inheritance
class manager:
    def __init__(self,Name,id,dep):
        self.name=Name
        self.id=id
        self.department=dep

    def show(self):
        print(f"My name is {self.name}\nmy id no is {self.id} \nand i am from {self.department} branch")

class employee(manager):
    def show1(self):
        print(f"i am working under {self.name}")

m1=manager("arun",36,"design")
m2=manager("om",3,"cse")
m3=manager("amol",64,"gaming")
m4=manager("karan",6,"security")

e=employee("amol",34,"developer")
e.show1()
# m1.show()
# m2.show()
# m3.show()          *-
# m4.show()

#days 62 access modifier

class student:
    def __init__(self):
        self.__newname="vaibhav"
    def detail(self):
        print("hii i am vaibhav")
obj=student()
print(obj._student__newname)
obj.detail()

#days 63 solution for snake water gun game

#days 64 library management system exercise 6

class Library:
    no_of_books = 0
    books = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
    "The Lord of the Rings by J.R.R. Tolkien",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Pride and Prejudice by Jane Austen",
    "The Catcher in the Rye by J.D. Salinger",
    "The Chronicles of Narnia by C.S. Lewis",
    "Animal Farm by George Orwell",
    "The Hobbit by J.R.R. Tolkien",
    "Fahrenheit 451 by Ray Bradbury",
    "Jane Eyre by Charlotte Brontë",
    "Wuthering Heights by Emily Brontë",
    "The Book Thief by Markus Zusak",
    "The Kite Runner by Khaled Hosseini",
    "Brave New World by Aldous Huxley",
    "The Hunger Games by Suzanne Collins",
    "The Fault in Our Stars by John Green",
    "Gone with the Wind by Margaret Mitchell",
    "Moby Dick by Herman Melville"
    ]


    def count(self):
        count=0
        for i in self.books:
            count+=1
        return count
    def Ismatch(self):
        if number_of_books==len(self.books):
            print("Matched")
        else:
            print("Not match")

# Create an instance of the Library class
library_instance = Library()

# Count and print the number of books
number_of_books = library_instance.count()

# Take books input
# library_instance.take()

print(f"Total number of books: {number_of_books}")
library_instance.Ismatch()

##days 65 static method
class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b


a=math(5)
a.addtonum(2)
print(a.num)
print(a.add(2,5))


##day 66 instance vs class variable
class employee:
    company ="tata"
    def __init__(self,name):
        self.name=name
        self.raised_amount=15

    def show(self):
        print(f"the name of the employee is {self.name} and he raised amount is {self.raised_amount} working in {self.company}")

emp1 =employee("vaibhav")
emp1.show()
employee.show(emp1)
emp2=employee("varun")
emp3=employee("arjun")
emp3.company="volvo"
emp2.show()
emp3.show()

#day 67 solve exercise 6

#day 68 exercise 7(clear and clutter)

import os
i=0
files=os.listdir("cluttered")
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluttered/{file}",f"cluttered/{i}.png")
        i=i+1


#day 69 pthon method

class employee:
    company = "apple"
    def show(self):
        print(f"my name is {self.name} and i am working in {self.company}")


    def newcompany(self,newname):
        self.company=newname

emp1=employee()
emp1.name="aman"
emp1.show()
emp1.newcompany("tata")

emp1.show()

#days 70 class method as aternative constructor

class hello:
    def __init__(self,name,sallary) :
       self.name=name
       self.sallary=sallary

    @classmethod
    def fromstr(self,string):
        return self(string.split("-")[0],string.split("-")[1])


ep1=hello("om",15000)
print(ep1.name)
print(ep1.sallary)

str="no-12000"
ep2=hello(str.split("-")[0],str.split("-")[1])
print(ep2.name)
print(ep2.sallary)


string ="komal-20000"
ep3=hello.fromstr(string)
print(ep3.name)
print(ep3.sallary)


#days 71 dir,dict,help

x=[6,7,3,4,6,674,3,2,3]

print(dir(x))
print(x.__add__)
print(help(x))
print("\n")
print("\n")
print("\n")
print("\n")

class method:#dictonay class
    def __init__(self,name,age):
        self.name=name
        self.age= age
fun1=method("vaibhav",20)
print(fun1.__dict__)
print("\n")
print("\n")
print("\n")
print("\n")
print(help(fun1))
# print(dir(x))
# print(dir(x))
# print(dir(x))


#days 72 super keyword
class university:
    def __init__(self,student,course):
        self.student=student
        self.course=course

    def detail(self,name,age,enroll):
        # name="om"
        # age=21
        # enroll=12634
        print(f"his name is {name} , and he is {age} year old and roll no is {enroll}")

class student(university):
    def __init__(self,student,course,enroll):
     self.enroll=enroll
     super().__init__(student,course)


std=student("vaibhav","btech",600)
std.detail("aman",20,15)
print(std.student)
print(std.enroll)
print(std.course)

#day 73 magic /dundle method(str,repr,call,len etc)
class Name:
    name="kalua"
    # print(len(name))
    def __len__(self):
       i=0
       for c in self.name:
           i=i+1
       return i

    def __str__(self):
       return f"the name of the boy is {self.name}"
    def __repr__(self):
       return f"the name of the man is {self.name}"

    def __call__(self):
       print("dont call me")


a= Name()
print(len(a))
print(a)
print(str(a))
print(repr(a))
a()


#days 74 method overriding

class department:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def detail(self):
        print(f"He is {self.name} and his roll no is {self.roll}")


class std(department):
    def __init__(self, name, roll, age, course):
        super().__init__(name, roll)  # Call the parent class's __init__ method
        self.age = age
        self.course = course

    def detail(self):
        print(f"He is {self.name}, his roll no is {self.roll}, he is {self.age} years old, and he is studying {self.course}")


dep = department("omkar", 24)

# Create an instance of std and call its detail method
student = std("Rahul", 25, 20, "Computer Science")
dep.detail()  # Call detail without arguments
student.detail()


#days 75 exercise 7 solution

#days 76 exercise 8 merge the pdf

from pypdf import PdfMerger
import os

# List of PDF files to merge
pdf_files = ["PDF1.pdf", "PDF2.pdf", "PDF3.pdf", "PDF4.pdf", "PDF5.pdf"]

# Create a PdfMerger object
merger = PdfMerger()

for pdf in pdf_files:
    if os.path.isfile(pdf):
        merger.append(pdf)
    else:
        print(f"Error: The file '{pdf}' does not exist.")

# Write the merged PDF to a file
try:
    merger.write("merged.pdf")
    print("Merged PDF created successfully.")
except Exception as e:
    print(f"Error writing the merged PDF: {e}")

# Close the PdfMerger object
merger.close()


#days 77 operator overloading

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,v2):
        return vector(self.i + v2.i, self.j+v2.j,self.k+v2.k)

    def __mul__(self,v2):
        return vector(self.i * v2.i, self.j*v2.j,self.k*v2.k)

v1=vector(1,2,3)
v2=vector(5,7,9)
v3=vector(4,5,6)
print(v1)
print(v2)
print(v3)
print(v1 + v2 + v3)
print(v1 * v2 * v3)

#day 78 single inhertance

class student:
    def __init__(self,name,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender
    def detail(self):
        print(f"name :{self.name} \nRoll Number :{self.rollno}\nGender :{self.gender}")

class department(student):
    def __init__(self, name, rollno, gender, course):
        super().__init__(name, rollno, gender)
        self.course = course

    def detail(self):
        super().detail()
        print(f"Course :{self.course}")


obj1=student("vaibhav",600,"male")
obj2=department("vaibhav",600,"male","cse")

obj1.detail()
# obj2.detail()


#days 79 multiple inhertance


class student:
    def __init__(self, name, rollno, gender):
        self.name = name
        self.rollno = rollno
        self.gender = gender

    def detail(self):
        print(f"name :{self.name} \nRoll Number :{self.rollno}\nGender :{self.gender}")


class department:
    def __init__(self, name, rollno, gender, course):
        self.name = name
        self.rollno = rollno
        self.gender = gender
        self.course = course

    def detail(self):
        print(f"name :{self.name} \nRoll Number :{self.rollno}\nGender :{self.gender}Course :{self.course}")


class address(student,department):
    def __init__(self, name, rollno, gender, course, address):
        student.__init__(self, name, rollno, gender)
        department.__init__(self, name, rollno, gender, course)
        self.address = address

    def __str__(self):
        return f"name :{self.name} \nRoll Number :{self.rollno}\nGender :{self.gender}\nCourse :{self.course}\naddress :{self.address}"


obj1 = student("vaibhav", 600, "male")
obj2 = department("vaibhav", 600, "male", "cse")
obj3 = address("vaibhav", 600, "male", "cse", "thane")

# obj1.detail()
# obj2.detail()
print(obj3)


#days 80 multi level inhertance

class student:
    def __init__(self, name, rollno, gender):
        self.name = name
        self.rollno = rollno
        self.gender = gender

    def detail(self):
        print(f"name :{self.name} \nRoll Number :{self.rollno}\nGender :{self.gender}")


class department(student):
    def __init__(self, name, rollno, gender, course):
        super().__init__( name, rollno, gender)
        self.course = course

    def detail(self):
        super().detail()
        print(f"Course :{self.course}")


class address(department):
    def __init__(self, name, rollno, gender, course, address):
        super().__init__(name, rollno, gender, course)
        self.address = address

    def __str__(self):
        super().detail()
        return f"address :{self.address}"


obj1 = student("vaibhav", 600, "male")
obj2 = department("vaibhav", 600, "male", "cse")
obj3 = address("vaibhav", 600, "male", "cse", "thane")

obj1.detail()
print("\n")
obj2.detail()
print("\n")
print(obj3)


#days 81 Hierarchical inheritance

class Animalia:
    def __init__(self, name):
        self.name = name
    
    def detail_animalia(self):
        print(f"His name is: {self.name}")

class Animal(Animalia):
    def __init__(self, species, name):
        super().__init__(name)
        self.species = species

    def detail_animal(self):
        super().detail_animalia()
        print(f"The species is: {self.species}")

class Dog(Animalia):
    def __init__(self, bark,name):
        super().__init__(name)
        self.bark = bark

    def detail(self):
        super().detail_animalia()
        print(f"It barks: {self.bark}")

# Create objects
obj = Animal("Labra", "Sonu")
obj1 = Dog("Barking",  "Kalya")

# Call detail methods
obj.detail_animal()
obj1.detail()



#hybrid inheritance
class Animalia:
    def __init__(self, name):
        self.name = name
    
    def detail_animalia(self):
        print(f"His name is: {self.name}")

class Animal(Animalia):
    def __init__(self, species, name):
        Animalia.__init__(self, name)  # Direct call to Animalia's init
        self.species = species

    def detail_animal(self):
        self.detail_animalia()
        print(f"The species is: {self.species}\n")

class Dog(Animalia):
    def __init__(self, bark, name):
        Animalia.__init__(self, name)  # Direct call to Animalia's init
        self.bark = bark

    def detail_dog(self):
        self.detail_animalia()
        print(f"It barks: {self.bark}\n")

class Doctor(Animal, Dog):
    def __init__(self, species, bark, d_name, name):
        Animalia.__init__(self, name)  # Initialize the topmost base class
        Animal.__init__(self, species, name)
        Dog.__init__(self, bark, name)
        self.d_name = d_name

    def detail(self):
        print(f"This is Dr. {self.d_name}\n")
        Animal.detail_animal(self)
        Dog.detail_dog(self)

# Create objects
obj = Animal("Labra", "Sonu")
obj1 = Dog("Barking", "Tisen")
obj2 = Doctor("Labra", "Barking", "Husmukh", "Rambo")

# Printing details
obj2.detail()
obj.detail_animal()
obj1.detail_dog()


#days 82 exercise 8 solution

#days 83 exercise 9

1.Write a program to pronounce list of names using win32 API.
2 If you are given a list l as follows:
3`````python
4 l = ["Rahul", "Nishant", "Harry"]
5 ````
6 Your program should pronouce:
7````
8 Shoutout to Rahul
9 Shoutout to Nishant



import win32com.client as wincl


speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
list1=["aman","Rohan","khushi","andry"]
for i in list1:
 spk.Speak("shoutout to "+i)


#days 84 time module

import time
time1=time.time()

for i in range(100):
    print(i)
        
time2=time.time()

i=0
while i <100:
    print(i)
    i=i+1 
        
print(time.time() - time1)
print(time.time() - time2)   
j=0
while j <10:
    time.sleep(2)
    print(j)
    j=j+1   
    
#priting current time
t=time.localtime()
t_format=time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(t_format)

##day 85 skip commom command line

##day 86 walrus opertor

# foods=list()
# while True:
#     foods=input("what food do you like?: ")
#     if foods=="exit":
#         break
    
#using walrus
foods=list()
while (food:=input("enter foods:") ) !="exit":
    foods.append(food)

#day 87 shutil module

import shutil
import os
shutil.copy("hello.txt","vaibhav.py")
shutil.copytree("aloo","vaibhav1.py")
shutil.move("hello.txt","aloo")
os.remove("aloo/hello.txt")

# day 88 exercise 9 solution


# day 89 request module

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data= {
    "title": 'harry',
    "body":'bhai',
    "userId": 12,
}

headers={
    'Content-type' : 'application/json;charset=UTF-8',
}

rsponse= requests.post(url,headers=headers , json=data)

# day 90 excise 10 with solution news api

import requests
import json

query=input("Enter what news you want:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-06-16&sortBy=publishedAt&apiKey=958bb3b2b30a4a4ba38cfadb87bb7e8f"
r= requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(f"TITLE :{article["title"]}")
    print(f"DESC :{article["description"]}")
    print("----------------------------------------------------------")


# day 91 python generator

def my_generator():
    for i in range(500):
        yield i

gen= my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("------End--------")


# day 92   function caching
from  functools import lru_cache
import time

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(2)
    return n*5


print(fx(2))
print("done for 2")
print(fx(5))
print("done for 5")
print(fx(7))
print("done for 7")
print(fx(3))
print("done for 3")
print(fx(8))
print("done for 8")


print(fx(2))
print("done for 2")
print(fx(5))
print("done for 5")
print(fx(7))
print("done for 7")
print(fx(3))
print("done for 3")
print(fx(8))
print("done for 8")

print(fx(100))

# day 93 exercise 10 solution

# day 94 exercise 11 drink water reminder
import time
import win32com.client as wincl


speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)


def drink_water_reminder(interval_in_minutes):


    interval_seconds = interval_in_minutes * 60
    while True:
        time.sleep(interval_seconds)
        spk.Speak("It's time to drink water!")
        print("It's time to drink water!")

if __name__ == "__main__":
    interval_minutes = 1  # Change this to set your reminder interval in minutes
    drink_water_reminder(interval_minutes)


# day 95 regalar expression

import re

pattern = r"[A-Z]cience"
text = "Cora Agnes Benneson (1851–1919) was an American attorney, lecturer, and writer. She graduated from the University of Michigan, earning a Bachelor of Arts in 1878, a Bachelor of Laws in 1880, and a Master of Arts in 1883, and was licensed to practice law in Illinois and Michigan. From 1883 to 1885, she traveled the world to learn about legal cultures and how they affected women. When she returned to the United States, she undertook a nationwide lecture tour to speak about her travels and observations. In 1886 Benneson briefly worked as an editor of West Publishing's law reports before taking up a history fellowship at Bryn Mawr College under then-professor Woodrow Wilson. In 1888 she moved to Boston, where she continued to write and lecture. She was licensed in Massachusetts in 1894 and opened a law practice. She was made a fellow of the Dcience Association for the Advancement of Science in 1899 and elected secretary  Acience of its Social and Economic Science Section in 1900."

matches = re.finditer(pattern, text)
for match in matches:
    # print(match)
  print(text[match.span()[0]:match.span()[1]])


#day 96  asynclo in python

import asyncio
import time

async def function1():
    await asyncio.sleep(2)
    print("fun1")

async def function2():
    await asyncio.sleep(2)
    print("fun2")

async def function3():
    await asyncio.sleep(2)
    print("fun3")

async def main():
    # Gather all the functions to run concurrently
    await asyncio.gather(
        function1(),
        function2(),
        function3()
    )

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

#day 97 multithreading in python

import threading
import time

def func(second):
    
    print(f"sleeping for {second} second")
    time.sleep(second)

#normal zindagi   
time1=time.perf_counter()
func(3)
func(2)
func(1)
time2=time.perf_counter()
print(time2-time1)


# #mentos zindagi
# t1=threading.Thread(target=func,args=[3])
# t2=threading.Thread(target=func,args=[2])
# t3=threading.Thread(target=func,args=[1])

# t1.start()
# t2.start()
# t3.start()

#day 98 multiprocessing

import multiprocessing
import requests

def downloadfiles(url, name):
    print(f"Downloading file {name}....")
    response = requests.get(url)
    with open(f"file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Downloaded file {name}!")

if __name__ == '__main__':
    url = "https://picsum.photos/200/300"
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=downloadfiles, args=(url, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    
#day 99 exercise 11 solution


#day 100 guide for what learn next


    





