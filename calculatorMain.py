import calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum: ", calculator.add(num1, num2))
print("Diff: ", calculator.subtract(num1, num2))
print("Prod: ", calculator.multiply(num1, num2))
print("Divide: ", calculator.divide(num1, num2))