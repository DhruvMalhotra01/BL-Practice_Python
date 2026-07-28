# PROG 2: To Implement Slicing

# Take input
string = input("Input string: ")

# Find first, middle and last characters
first = string[0]
middle = string[len(string) // 2]
last = string[-1]

# Create new string
result = first + middle + last

# Display output
print("Output string containing first, middle and last character:", result)