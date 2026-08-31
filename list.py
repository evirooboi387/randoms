list_values = []
list_values.append(20)
list_values.append(10)
list_values.append(30)
list_values.append(40)

list_values = [20, 10, 30, 40]

# List search: O(n), or linear time.

set_values = set()
set_values.add(10)
set_values.add(20)
set_values.add(30)
set_values.add(40)

for value in set_values:
    print(value)

# Set lookup: O(1) on average, or constant time.

dict_values = {}
dict_values["a"] = 10
dict_values["b"] = 20
dict_values["c"] = 30
dict_values = {"a": 10, "b": 20, "c": 30}

# A simple hash-table bucket illustration:
buckets = {
    0: [],
    1: [10],
    2: [20],
}


str=abc :0->a,1->b,2->c
str[0] = 'a'

tuple_values = (10, 20, 30, 40)