# Write a Python function to flatten a nested list.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]


def flatten():
    x = [[1, 2], [3, 4], [5]]
    y = []

    for i in x:
        for j in i:
            y.append(j)
    return y

print(flatten())

# Merge Two Sorted Lists
# Write a Python function to merge two sorted lists into a single sorted list.
# Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

def merge():
    a = [1, 3, 5]
    b = [2, 4, 6]
    c = []
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    while j<len(b):
        c.append(b[j])
        j=j+1

    print(c)

merge()


# Find All Pairs in a List that Sum to a Specific Value
# Write a Python function to find all pairs in a list that sum to a specific value.
# Input: [1, 2, 3, 4, 5], Sum=6
# Output: [(1, 5), (2, 4)]
def pairs():
    a = [1, 2, 3, 4, 5]
    target = 6
    result = []

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]+a[j]==target:
                result.append((a[i],a[j]))
    print(result)
pairs()