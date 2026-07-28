import datetime

# Date as string
date_string = "27 Jul 2026"

print("Date as Date String:", date_string)
print(type(date_string))

# Convert string to datetime object
date_object = datetime.datetime.strptime(date_string, "%d %b %Y")

print()
print("Date as DateTime object:", date_object)
print(type(date_object))

# Convert datetime object back to string
date_string_again = date_object.strftime("%d %b %Y")

print()
print("Date back to as Date String:", date_string_again)
print(type(date_string_again))