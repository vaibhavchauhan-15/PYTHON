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
