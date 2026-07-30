a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Display initial values
print("\nInitial Value of a & b are")
print("a: ", a)
print("b: ", b)

# Traditional swapping using a temporary variable
temp = a
a = b
b = temp

# Display values after swapping
print("\nAfter traditional swapping:")
print("a = ", a)
print("b = ", b)