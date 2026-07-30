square_list = [num ** 2 for num in range(10)]

# Convert the list into a tuple using tuple() constructor
square_tuple = tuple(square_list)

# Display the list
print("The List of Square of Numbers is", square_list)

print("Use of index for accessing elements in tuple")

# Access specific elements using indexing
print("3rd element:", square_tuple[2])
print("5th element:", square_tuple[4])
print("7th element:", square_tuple[6])

# Access first three elements using slicing
print("First 3 elements:", square_tuple[:3])