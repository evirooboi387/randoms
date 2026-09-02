def find_max_min(numbers):
    max=numbers[0]
    min=numbers[0]

    for num in numbers:
        if num> max:
            max=num
        if num<min:
            min=num
    return (max,min)

x=[3,1,4,1,5,9]
output= find_max_min(x)
print(output)

# x=[3,1,4,1,5,9]
# max=x[0]
# min=x[0]
#
# for i in x:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print(max,min)



print("*****************")

y=[1,2,2,3,4,4,5]
o=y[0]
for i in y:
    if i==o:
        o=i
print(o)