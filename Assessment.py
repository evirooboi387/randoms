# question1
a = "python"
d = ""
for i in a:
    d=i+d
print(d)

# question2
y = "programming"
for i in y:
    if y.count(i)==1:
        print(i)
        break

# question3
word="madam"
t=""

for i in word:
    t=i+t
if word==t:
    print(True)
else:
    print(False)

# question4
h="hello"
r=""
for i in h:
    if i not in r:
        count=0
        for j in h:
            if i==j:
                count+=1
        r+=i+":"+str(count)+" "
print(r)

# question5
a = "programming"
s = ""

for i in a:
    if i not in s:
        s += i
print(s)

# question6
q = [1, 2, 2, 3, 4, 4]
w = []

for i in q:
    if i not in w:
        w.append(i)
print(w)

# question7
numbers = [10, 20, 5, 30, 25]

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)


# question8
numbers = [1, 2, 3, 2, 4, 5, 1]
duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

# question9
numbers = [1, 2, 3, 4, 5]
k = 2

result = []

for i in range(len(numbers) - k, len(numbers)):
    result.append(numbers[i])

for i in range(0, len(numbers) - k):
    result.append(numbers[i])

print(result)

# question10
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = []

for i in a:
    if i in b:
        result.append(i)

print(result)

# question11
numbers = [1, 2, 2, 3, 3, 3]
d = {}

for i in numbers:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# question12
d = {"A": 100, "B": 500, "C": 300}

maximum = 0
result = ""

for i in d:
    if d[i] > maximum:
        maximum = d[i]
        result = i

print(result)

# question13
d = {"a": 1, "b": 2}
result = {}

for key in d:
    result[d[key]] = key

print(result)

# question14
d1 = {"a": 1}
d2 = {"b": 2}

result = {}

for i in d1:
    result[i] = d1[i]

for i in d2:
    result[i] = d2[i]

print(result)

# question15
sentence = "python is good python is easy"
words = sentence.split()

d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# question16
for i in range(1, 6):
    print("*" * i)

# question17
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# question18
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)

# question19
for number in range(2, 101):
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number)

# question20
n = 8

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# question21
numbers = [1, 2, 3, 4, 5, 1, 2, 3]

for i in numbers:
    if numbers.count(i) == 1:
        print(i)
        break

# question22
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
n = 2

count = 0

for i in numbers:
    if numbers.count(i) == 1:
        count += 1

        if count == n:
            print(i)
            break

# question23
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print(True)
else:
    print(False)

# question24
numbers = [1, 2, 3, 5]

for i in range(1, 6):
    if i not in numbers:
        print(i)
        break

# question25
numbers = [1, 2, 2, 3, 3, 3, 4]

top = numbers[0]
maximum = 0

for i in numbers:
    count = numbers.count(i)

    if count > maximum:
        maximum = count
        top = i

print(top)



