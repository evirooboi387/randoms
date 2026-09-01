list = {10, 20, 30, 20, 32, 48}
d = {}
for x in list:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)
print("********")
max = 0
list = {10, 20, 30, 20, 32, 48}
for x in list:
    if x > max:
        max = x
print(max)


print("**********************")



list=[10,20,30,20,30,30]
d={}
for x in list:
    if x in d:
        d[x]=d[x]+1
    else:
        d[x]=1
print(d)

for key in d:
    vaule= d[key]
    print(key, vaule)





print("**********")
max=0
max_num=0
for key in d:
    value=d[key]
    if value>max:
        max=value
        max_num=key
print(max_num, max)


line="hello world hello nepal hello india"
words=line.split(' ')
print(words)

words_dict={}
for x in words:
    if x in words_dict:
        words_dict[x]=words_dict[x]+1
    else:
        words_dict[x]=1
print(words_dict)
word_count=0
word_num=""
for key in words_dict:
    value=words_dict[key]
    if value>word_count:
        word_count=value
        word_num=key
print(word_num, word_count)

count=0
vowels=['a','e','i','o','u']
input="hello world"
for ch in input:
    if ch in vowels:
        count=count+1
print(count)

list1=['a','b','c']
list2=[1,2,3]
d={}
for i in range(len(list1)):
    value1= list1[i]
    value2= list2[i]
    d[value1]= value2
print(d)



