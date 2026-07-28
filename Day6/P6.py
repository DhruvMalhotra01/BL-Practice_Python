import re

# Take input
email = input("Enter an email address: ")

# Regular expression for email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Check if email is valid
if re.fullmatch(pattern, email):
    print(f"{email} is a Valid Email Address.")
else:
    print(f"{email} is an Invalid Email Address.")

