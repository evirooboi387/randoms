a = [1, 2, 3, 4, 5]
b = 0
for i in a:
    b= i+b
print(b)

a = [1, 2, 3, 4, 5, 6]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)

a = [10, 15, 20, 25, 30, 35, 40]
c=[]
for i in a:
    if i%2==0 and i>20:
        c.append(i)
print(c)

students = {
    "John": 75,
    "Mike": 82,
    "Sarah": 91,
    "David": 68,
    "Emma": 88
}
b={}
for name, score in students.items():
    if score>=80:
        b[name]=score
print(b)
