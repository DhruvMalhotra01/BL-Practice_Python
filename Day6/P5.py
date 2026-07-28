import re

# Take input
text = input("Enter a string: ")

# Find all digits
digits = re.findall(r'\d', text)

# Display result
if digits:
    print("Digits found in the string:", digits)
else:
    print("No digits found in the string.")