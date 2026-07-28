text = input("Input String: ")

# Using list comprehensions
letters = [ch for ch in text if ch.isalpha()]
digits = [ch for ch in text if ch.isdigit()]
special = [ch for ch in text if not ch.isalpha() and not ch.isdigit()]

# Display result
print("Number of letters:", len(letters))
print("Number of digits:", len(digits))
print("Number of special symbols:", len(special))