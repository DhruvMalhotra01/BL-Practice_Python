text = input("Input String : ")

letters , digits , special = 0,0,0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special +=1

# Display result
print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of special symbols:", special)

# PS C:\Users\DELL\Desktop\BridgeLabzPython\Day6> python P3.py
# Input String : Dhruv123%%
# Number of letters: 5
# Number of digits: 3
# Number of special symbols: 2