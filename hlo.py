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

# # # #DAY 21
# # def avg(a=2,b=3):#default argument
# #     sum=0
# #     sum=(a+b)/2
# #     print("average is :",sum)
# # avg()
# # avg(5)
# # avg(5,6)


# # def NAMEPRINT(fname="aman",mname="kamal",lname="kumar"):# default argument
# #     print("hello!",fname,mname,lname)

# # NAMEPRINT()
# # NAMEPRINT("KOMAL")
# # NAMEPRINT("KOMAL","ramji")
# # NAMEPRINT("sanjana","akhilesh ","chauhan")

# #day22 LIST
# # a=[1,2,4,5,5,2,5,7,3,7,9,7,5,4,3,3,4]
# # name=["ram","mohan","kali","windows"]
# # print(a)
# # print(a[-1])
# # print(a[1:5])
# # print(a[1:8:2])
# # print(a[1:-1:2])
# # print(name)
# # print(name[1])
# # print(name[1:5])
# # print(name[1:8:2])
# # if "ram" in name:
# #     print("yes")











      




      
