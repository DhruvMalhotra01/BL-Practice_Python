a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Display initial values
print("\nInitial Value of a & b are")
print("a: ", a)
print("b: ", b)

# Pythonic swapping using tuple packing and unpacking
a, b = b, a

# Display values after swapping
print("\nAfter pythonic swapping:")
print("a = ", a)
print("b = ", b)