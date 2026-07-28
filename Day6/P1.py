list = []
for i in range(5):
    place = input(f"Enter the name of place {i + 1} : ")
    list.append(place)

print(list)

result = " , ".join(list).upper()
print(result)