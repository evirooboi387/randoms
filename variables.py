#
# data=[10,20,20,30,31,39]
# print(data)
# print (len(data))
# for x in data:
#    print(x)
# print("*")
# for x in data:
#     if x>= 30:
#         print(x)
# print("*")
#
# for x in data:
#     if x<30:
#         print(x)
# print("*")
#
# for x in data:
#     if x%2==0:
#         print(x)
# print("*")
# for x in data:
#     if x%2==1:
#         print(x)
# print("*")
#
# for x in data:
#     if x%2==1 & x>35:
#         print(x)
# print ("*")
#
# for x in data:
#     if x%2==1 | x<20:
#         print(x)
#
# print("*")
# data=[10,20,20,30,31,39]
# count2=0
# count3=0
# occurence=[]
#
# for x in data:
#     if x==20:
#         count2=count2+1
#         occurence.append(count2)
#     if x==30:
#         count3=count3+1
#         occurence.append(count3)
# print(count2, count3)
# print(occurence)
# print(20,count2,30,count3)
#
# d={}
# d[20]=1
# print(d)
# d[30]=1
# print(d)
# d[20]=d[20]+1
# d[30]=d[30]+1
# print(d)
# print(20 in d)
# print(50 in d)
#
# data=[10,20,20,30,31,39]
# d1={}
# for x in data:
#     if x in d1:
#         d1[x]=d1[x]+1
#     else:
#         d1[x]=1 #{10:1}
# print(d1)
#
#
# print("*******************************************************")
#
# list={10,20,30,20,32,48}
# d={}
# for x in list:
#     if x in d:
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# print(d)
# print("********")
# max=0
# list={10,20,30,20,32,48}
# for x in list:
#     if x>max:
#         max=x
# print(max)
# print("**********************")
# max= list[0]
# list={-10,-20,-30,-20,-32,-48}
# for x in list:
#     if x>max:
#         max=x
# print(max)


# Variables
x=5
y="John"
print(x)
print(y)

# Casting
x=str(3)        #x will be 3
y=int(3)        #y will be 3
z=float(3)      #z will be 3.0

x=5
y="John"
print(type(x))
print(type(y))

x="John"
#is the same as
x='John'


a=4
A="Sally"
#A will not overwrite a


#many values to multiple variables
x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x=y=z="Orange"
print(x,y,z)

#unpack a collection
fruits=["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#output variables
x="Python is awesome"
print(x)
print("PYTHON IS AWESOME")

x="Python"
y="is"
z="awesome"
print(x,y,z)
print("***********")


#Global variables
x="awesome"

def myfunc():
    print("Python is "+x)
myfunc()

print("******")
x="awesome"
print("Python is "+x)

myfunc()
myfunc()
myfunc()


#datatypes

x="Hello world"
x=20
x=3.33
x=1j
x=["apple","banana","cherry"]
x=("apple","banana","cherry")
x=range(6)
x={"name":"Riwaj","age":28}
x={"apple","banana","cherry"}
x=True


#Multiple strings
a="""Lorem ipsum dolor sit amet,
   consectetur adipiscing elit."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b="Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b[-5:-2])

r=" riwaj "
print(r.upper())
print(r[-4:-2])

a=" Hello, world! "
print(a)
print(a.strip())
a="Hello Kanxa"
print(a.replace("H","J"))

a="Hello, Wo®rld!"
print(a.split(",")) #returns ['Hello','World']
s="Hello"
b="World"
c=s+b
print(c)
c=s+" "+b
print(c)

age=28
txt="my age is {}"
print(txt.format(age))

quantity=3
itemno=567
price=49.33
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

myorder="I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))


print(10>9)
print(10 ==9)
print(10<9)

a=200
b=33

if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")


bool("abc")
bool(123)
bool(["apple","cherry","banana"])
bool(False)
bool(0)
bool("")
bool([])

x=1
y=5.5
z=-343543421245
print(type(x))
print(type(y))
print(type(z))

#Type conversion
x=1
y=3.4
a=float(x)
b=int(y)

print(a)
print(b)

print(type(a))
print(type(b))

import random
print(random.randrange(1, 33))
print(random.randrange(7,77))

print(10+5)
