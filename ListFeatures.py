'''
This is the documentation of the list
'''

num_list = []
print(num_list.__doc__)
# For insertion use -> Append, Extend, Insert

num_list.append(54)
print(num_list)

num_list.extend([23,34,45,56])

print(num_list)

num_list.remove(34)
print(num_list)
print(num_list.pop(2))
# num_list.clear()
print(num_list)

for num in num_list:
    print(num, end = " ")

for index , value in enumerate(num_list):
    print(f"List hold {value} at {index} index.")

for i in range (0, len(num_list),1):
    print(num_list[i])


num_list.sort()
num_list.reverse()