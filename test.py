
data=[10,20,20,30,31,39]
print(data)
print (len(data))
for x in data:
   print(x)
print("*")
for x in data:
    if x>= 30:
        print(x)
print("*")

for x in data:
    if x<30:
        print(x)
print("*")

for x in data:
    if x%2==0:
        print(x)
print("*")
for x in data:
    if x%2==1:
        print(x)
print("*")

for x in data:
    if x%2==1 & x>35:
        print(x)
print ("*")

for x in data:
    if x%2==1 | x<20:
        print(x)

print("*")
data=[10,20,20,30,31,39]
count2=0
count3=0
occurence=[]

for x in data:
    if x==20:
        count2=count2+1
        occurence.append(count2)
    if x==30:
        count3=count3+1
        occurence.append(count3)
print(count2, count3)
print(occurence)
print(20,count2,30,count3)

d={}
d[20]=1
print(d)
d[30]=1
print(d)
d[20]=d[20]+1
d[30]=d[30]+1
print(d)
print(20 in d)
print(50 in d)

data=[10,20,20,30,31,39]
d1={}
for x in data:
    if x in d1:
        d1[x]=d1[x]+1
    else:
        d1[x]=1 #{10:1}
print(d1)


print("*******************************************************")

list={10,20,30,20,32,48}
d={}
for x in list:
    if x in d:
        d[x]=d[x]+1
    else:
        d[x]=1
print(d)
print("********")
max=0
list={10,20,30,20,32,48}
for x in list:
    if x>max:
        max=x
print(max)
print("**********************")
max= list[0]
list={-10,-20,-30,-20,-32,-48}
for x in list:
    if x>max:
        max=x
print(max)





