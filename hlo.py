a=input("enter your number :")      
print("your name is :",a)   
x= int (input("enter first number :"))       
y=int (input("enter second number :"))       
       
print("addition :" ,x + y)            
print("subtraction :",x - y)          
print("divide :" ,x / y)         
print("multiplication :",x * y)        
print("reminder :" ,x % y)            
 
day 11              
andry = '''vaibhav'''          
for character in andry:    
 print(character)
      
      
#day 12   
names = "ankit ka bacchi" 
print(names[0:9]) 
print(len(names))
print(names[0:15:2])
print(names[:])   
print(names[2:10]) 
print(names[3:-1]) 
print(names[-5:-2]) 
print(names[0:-6]) 

# day 13
# string are unmutable
str ="Vaibhav"
print (str.upper())
print(str.lower())
print(str.rstrip('v'))
print(str.lstrip('V'))
print(str.replace('Vaibhav','khushi'))
print(str.split("b"))
str1="vaibhav chauhan"
print(str1.capitalize())
print(str1.title())
print(len(str1))
print(len(str1.center(50))) 
print(str1.count("vaibhav"))
print(str.startswith("V"))
print(str.endswith("v"))
print(str.endswith("a",1,5))
print(str.find("ai"))
print(str.index("ai"))
str = " hlo ji kya hal chal"
str2= "     " 
print(str.isalnum())
print(str.isalpha())
print(str.islower())
print(str.isupper())
print(str.isprintable())
print(str2.isspace())
print(str.istitle())
print(str.swapcase())

#DAY 14
#if ,else,elif
a=int(input("apna age btao babua: "))
if(a>=18 and a<60):
    print("vote mujhe hi dena")
elif(a>+60):
    print("are dada ji aram karo jakar thodi si to zindagi bachi hai")    
else:
    print("jakar complaint piyo")  


#DAY 15
a = int(input("enter the hour till 12 am in 24H format:"))
if(a<=12):
    print("GOOD MORNING BHAI JI!")
elif(a>=12 and a <=16):
    print("GOOD AFTERNOON BHAIYA JI!")    
elif(a>=16 and a<20):
    print("GOOD EVENING BHAI JI!")
elif(a>=20  and a<=24):
    print("GOOD NIGHT JI!")
else:
    print("andhera kayam rahe!")            

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


# DAY 16
# match case statement

print("press 1 for morning:\npress 2 for afternoon:\npress 3 for evening:\npress 4 for night:")
a= int (input("enter your choice:"))
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
        print("bye bye")               


# DAY 17
# FOR LOOP

name = "hariom prashad rajkumar"
for i in name:
    print(i ,end=",")

name = " vaibhav chauhan"
for i in name:
    print(i)

for num in range(10):#range
    print(num)

for num in range(10,15):#range
    print(num)  

for num in range(10,20,2 ):#step
    print(num)
# DAY 18
n=int(input("Enter a number how many times you want to print :"))
a=0
while(a<=n):
 print("hii")
 a +=1

       
do {
  print("hlo")
}
while()
  

count=5
while(count>0):
 print(count) 
count -=1
 
#DAY 19
for i in range(1,11):
    if(i==5):
     continue
    print("5 X",i,"=",5*i)
    if(i==10):
        break

# DAY 20
# function
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
def isgreater(a,b):
    if(a>b):
        print("a bara hai")
    else:
        print("b bara hai ") 

def isless(a,b):
    if(a<b):
        print("a is small")
    else:
        print("b is small or equal")

def avg(a,b):
    c=0
    c=(a+b)/2
    print("This is the avg value :",c)

def Table(a):
    for i in range(10):
        print(a,' x ',i+1,'= ',a*(i+1)) #5 x 1 = 5 
        i=i+1   
                 

isgreater(a,b)  
isless(a,b)
avg(a,b)
Table(a)

# #DAY 21
def avg(a=2,b=3):#default argument
    sum=0
    sum=(a+b)/2
    print("average is :",sum)
avg()
avg(5)
avg(5,6)


def NAMEPRINT(fname="aman",mname="kamal",lname="kumar"):# default argument
    print("hello!",fname,mname,lname)

NAMEPRINT()
NAMEPRINT("KOMAL")
NAMEPRINT("KOMAL","ramji")
NAMEPRINT("sanjana","akhilesh ","chauhan")

#day22 LIST
a=[1,2,4,5,5,2,5,7,3,7,9,7,5,4,3,3,4]
name=["ram","mohan","kali","windows"]
print(a)
print(a[-1])
print(a[1:5])
print(a[1:8:2])
print(a[1:-1:2])
print(name)
print(name[1])
print(name[1:5])
print(name[1:8:2])
if "ram" in name:
    print("yes")

#palindrome or not

value = input("Enter a value: ")
n = value[::-1]
if(value == n):
    print("it is palindrome")
else:
    print("no palindrome")   

# DAY 23 list
l = [ 1,5,8,6,9,5,8,5,3,8]
print(l)
l.append(7)
print(l,"after append")
l.sort()
print(l,"after sort")
l.sort(reverse=True)
print(l,"after reverse sort")
print(l.index(1)) #print the index of 1
print(l.count(5)) #counting the value
# m=l
# m[8]=0
# print(l)
l.insert(3,777)
print(l,"after insert 777")
m=[44,665,9656]
l.extend(m)
print(l,"after extend")

# day 24 tuple 
tup = (45,87,69,57,46,32,78)
print(type(tup),tup)
print(len(tup),"length of tuple")
# tup[3]=4  tuple is immutable
print(tup[1])
print(tup[-1])
print(tup[5])
# print(tup[8]) out of range 
print(tup[:6])
tup2 = tup[ :3]
print(tup2)

# day 25
tup = [45,87,32,69,57,46,32,78]
country = ("india","japan","uk","finland","saudi")
name = ("ram","sita","lakshman","hanuman")
temp = list(country)
temp.append("kuwait")
temp.pop(2)
temp[3]="baigan"
temp.extend(tup)
country = tuple(temp)
print(country,"\n\n")
final = country + name
print(final,"\n\n")
temp2 = tup.count(45)
print(temp2)
temp3 = tup.index(32,3,8)
print(temp3)
temp3 =len(tup)
print(temp3)


# day 26 
import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
hour = int(input("Enter hour :"))
print(hour)
if(hour >= 0 and hour < 12):
    print("GOOD MORNING SIR!")
elif(hour >= 12 and hour <16):
    print("GOOD AFTERNOON SIR!")
elif(hour >=16 and hour <=19):
    print("GOOD EVENING SIR!")
elif(hour > 19 and hour <=24):
    print("GOOD NIGHT SIR!")    

#day 27 do some exercise

#day 28 f"string
letter = "My name is {2} and \nI am from {1}\nI am {0} old"
name = "Vaibhav chauhan"
place = "Bihar"
age=19
print(letter.format(age,place , name))
print(f"\n\nUSING F STRING LIKE THIS: \n\nMy name is {{name}} and \nI am from {{place}}\nI am {{age}} old")
print(f"\n\nUSING F STRING \n\nMy name is {name} and \nI am from {place}\nI am {age} old")

price=84.034254
print(f"The price of doller is :{price :.2f}")

# DAY 29 Docstring
def sum(a,b):
    '''Add two integer and return the sum value'''
    s=a+b
    return s

a=5
b=4
print(sum(a,b))
print(sum.__doc__)

# DAY 30 RECURSION 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))    



def fabonacci(n):
 if(n==0 or n==1):
    return 1
 else:
   return  fabonacci(n -1) + fabonacci(n -2)

print(fabonacci(5))


# DAY 31 SETS

name  = {"ram","shyam","jon","ram","jack","shyam"}
print(name)

for i in (name):
   print (i)

   
tpye1={}
type2=set()
print(type(name))
print(type (tpye1))
print(type (type2) ) 

# day 32 sets method
     
cities = {"vadodara","thane","surat","kutch"}
state = {"gujrat","bihar","maharashtra","assam","kerala"}
state2={"jammu","kashmir","ladak","bihar","assam","gujrat"}
state3={"jammu","kashmir"}
# print(type(state))
print(state.difference(state2))
print(state2.difference(state))
print(state.union(state2))
# state2.update(state)
print("after update\n",state2)
print("after intersection:\n",state.intersection(state2))
print("after symmetric_difference:\n",state.symmetric_difference(state2))
# print("after symmetric_difference:\n",state.symmetric_difference_update(state2))
# print(state)
print("disjoin:",state.isdisjoint(cities))
print("disjoin:",state.isdisjoint(state))
print("superset:",state2.issuperset(state3))
print("subset:",state3.issubset(state2))
state3.add("har har mahadev")
print("after add:",state3)
state3.remove("har har mahadev")
print("after remove:",state3)
# state3.remove("har har mahadev")#it show error if does'n exist
# state3.discard("har har mahadev")#it doesn't show error if does'n exist
print(state3)
item = state3.pop()
print("after pop:",state3)
print(item)
state3.clear()
print(state3)
# del state3
# print(state3)#now state3 doesn't exist



#day 33 dictonary

dic = {
    'name':'vaibhav',
    'age': 19,
    'weight':500
}

info = {1:'student1'' grade A',2:'student2'' grade A',3:'student3'' grade B'}
print(dic)
print(info)
print(info[2])
print(info.keys())
print(info.values())
for i in info.values():
    print(i)




# day 34 dictonary method 
std1 = {600:68, 297: 90, 65: 85, 75: 00}
print(std1)
std2 = {635:64, 227:50 ,785:55,855:707,58:55,655:20}
print(std2)
print(std1[65])

std2.popitem()
print("after pop item:",std2)
std1.pop(65)
print("after pop:",std1)

std2.update(std1)
print("after update:",std2)
std2.clear()
print("after clear:",std2)
del std1[600]
print("after delete item:",std1)
#printing index value
print(std1.get(0))
print(std1.get(3))
print(75)
# del std1
# print("after delete:" ,std1) #raised error

#day 35 for loop with else statement

for i in range(5):
    print(i)
    if i == 4:
        break 
    
else:
    print("else block") 
    

i=0     
while(i<5):
    print(i)
    i=i+1
else:
    print("else block")

i=0   #with break  
while(i<5):
    print(i)
    i=i+1
    if i==3:
     break
else:
    print("else block")



#day 36 exception handling

n=input("enter the number :")
print(f"multiplication of {n} is:")

for i in range(1,11):
    print(f" {n} x {i} = {int(n)*i}")
    
#using exception handling
n=input("enter the number :")

try:
   print(f"multiplication of {n} is:")  
   for i in range(1,11):
     print(f" {n} x {i} = {int(n)*i}")
     
     
except Exception as e:
  print(e)

#day 37 finally keyword


try:
    l=[1,2,5,3,2,6]
    i=int(input("enter the index number:"))
    print(l[i])
except IndexError as e:
    print(e)  
    
finally:
    print("finally block")     

def fun1():
    try:
     l=[1,2,5,3,2,6]
     i=int(input("enter the index number:"))
     print(l[i])
    except IndexError as e:
     print(e)  
    
    finally:
        print("finally block") 
    
    
#days 38 custom errors

# n=int(input("enter num between 5 and 9:"))

# if(n<5 or n>9) :
#     raise ValueError("invalid input")   


try:
    n=int(input("enter num between 5 and 9:"))

    if(n<5 or n>9) :
        raise ValueError("invalid input") 
    
except Exception as e:
    print(e)
        
        
        
#days 39 create kbc

questions = [
    {
        "question": "Who is the first Prime Minister of India?",
        "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Indira Gandhi", "D) Sardar Patel"],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A) 90°C", "B) 100°C", "C) 120°C", "D) 80°C"],
        "answer": "B"
    }
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




# #is prime or not
# def is_prime(n):
#     if n <= 1:
#         return "not prime"
#     if n <= 3:
#         return "prime"
#     if n % 2 == 0 or n % 3 == 0:
#         return "not prime"
    
#     k = 1
#     while True:
#         check1 = 6 * k - 1
#         check2 = 6 * k + 1
        
#         if check1 * check2 > n:
#             return "prime"
        
#         if n % check1 == 0 or n % check2 == 0:
#             return "not prime"
        
#         k = k + 1

# # Taking input from the user
# n = int(input("Enter a number which you want to check prime or not: "))
# result = is_prime(n)
# print(result)


#binary search

# arr = [1, 3, 6, 7, 9, 11, 12, 15, 16, 18, 21]
# left = 0
# right = len(arr) - 1

# # Display the array elements
# for i in range(len(arr)):
#     print(arr[i])

# target = int(input("Enter any number from the above list: "))

# # Binary search implementation
# while left <= right:
#     mid = left + (right - left) // 2
    
#     if target == arr[mid]:
#         print(f"Element {target} is found at index {mid}.")
#         break
#     elif target < arr[mid]:
#         right = mid - 1
#     else:
#         left = mid + 1
# else:
#     print(f"Element {target} is not found in the list.")
# arr = [1, 3, 6, 7, 9, 11, 12, 15, 16, 18, 21]
# left = 0
# right = len(arr) - 1

# # Display number
# print("Array elements:", arr)

# target = int(input("Enter any number from the above list or a new number to insert: "))

# # Binary search 
# found = False
# while left <= right:
#     mid = left + (right - left) // 2
    
#     if target == arr[mid]:
#         print(f"Element {target} is found at index {mid}.")
#         found = True
#         break
#     elif target < arr[mid]:
#         right = mid - 1
#     else:
#         left = mid + 1

# # If the element is not found, insert it in the correct position
# if not found:
#     print(f"left at {left} position")
#     arr.insert(left, target)
#     print(f"Element {target} is not found in the list. It has been inserted at index {left}.")
#     print("New array elements:", arr)


#day40 encryption and decryption

import random
import string

def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        modified_word = word[1:] + first_letter
        random_prefix = ''.join(random.choices(string.ascii_letters, k=3))
        random_suffix = ''.join(random.choices(string.ascii_letters, k=3))
        encoded_word = random_prefix + modified_word + random_suffix
    else:
        encoded_word = word[::-1]
    return encoded_word

def decode_word(word):
    if len(word) < 3:
        decoded_word = word[::-1]
    else:
        stripped_word = word[3:-3]
        last_letter = stripped_word[-1]
        decoded_word = last_letter + stripped_word[:-1]
    return decoded_word

def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

# Example usage
original_message =input("Enter the message:") 
encoded_message = encode_message(original_message)
decoded_message = decode_message(encoded_message)

print("Original Message: ", original_message)
print("Encoded Message: ", encoded_message)
print("Decoded Message: ", decoded_message)

# #day 41 sort hand if else statement
a=5
b=3
print("A") if a>b else print("=") if a<b else print("B") 


c=9 if a>b else 10
print(c)


days 42 enumerate function
marks=[12,34,64,24,26,75,96,32,65,98,57]
index=0
for mark in marks: #want index and element both at a time
    print(mark)
    if index==6:
        print("awesome")
    index+=1  

  
#now using enumerate function
marks=[12,34,64,24,26,75,96,32,65,98,57]
for index,mark in enumerate(marks):
    print(mark)
    if index==6:
        print("awesome")


# #days 43 virtual environment

#days 44 import in python
# import math
# from math import pi,sqrt
import math as m
import pandas
# import math * # * means all but this is not recommanded
print(m.sqrt(5)*m.pi)
from DAA import daa  #this file and method create in the local file
daa()


#days 45 if __name__ = "__main__"
import vaibhav #this file create by me
vaibhav.welcome()

#days 46 os module in python


import os
print(os.getcwd())
if (not os.path.exists("oslist")):
  os.mkdir("oslist")
  
# for i in range(1,10): #file created
#     os.mkdir(f"oslist/list{i}")  

os.rename(f"oslist/day1",f"oslist/list1")

# for i in range(1,10):
#   os.rename(f"oslist/list{i}", f"oslist/day{1}")


#days 47 exercise 4 encryption and decription

coding = int(input("1 for encode and 0 for decode:"))
st = input("Enter your message:")
words = st.split(" ")

coding=True if (coding==1) else False
newwords = []
if(coding):
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
    if (len(word)>=3):
      st=word[3:-3]
      st=word[-1]+word[:-1]
      newwords.append(st)
    else:
      newwords.append(word[::-1])
print(" ".join(newwords))


#days 48 local and global variable

x=4
y=9 #global variable

print(f"global variable x={x}")
def fun():
  z=5 #local variable
  global x
  x=10
  print(f"local variable z={z}")

fun()
print(f"global variable y={y}")
print(f"global variable x={x}")
# print(z)#give error because this is loacal
          # variable it cannon use in outside the function

# days 49 file io in python

# f=open('hello.txt','r')
# # f.write('hii i am vaibhav')
# # f.close()
# seen=f.read()
# print(seen)
# f.close()

try:
    f=open('hello.txt', 'r')
    seen = f.read()
    print(seen)
except FileNotFoundError:
    print("The file 'hello.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


#days 50 read(),readlines(),and other method

f=open('hello.txt','r')

while True:
    line = f.readline()#use for read a single line
    if not line:
        break
    print(line)
    print("\n")
lines = f.readlines()#use for read a multiples line
lines = f.writelines()#use for write  multiples line
print(lines)


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


    





