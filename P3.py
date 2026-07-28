import datetime

# Get current date and time
now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Formatted Date and Time:")

print("Month (as full name):", now.strftime("%B"))
print("Weekday (as full name):", now.strftime("%A"))
print("Year (as four digits):", now.strftime("%Y"))

print("Month (as abbreviated name):", now.strftime("%b"))
print("Weekday (as abbreviated name):", now.strftime("%a"))
print("Year (as two digits):", now.strftime("%y"))

print("Day of the month (01-31):", now.strftime("%d"))
print("Hour (24-hour clock):", now.strftime("%H"))
print("Hour (12-hour clock):", now.strftime("%I"))
print("Minute (00-59):", now.strftime("%M"))
print("Second (00-59):", now.strftime("%S"))
print("AM/PM indicator:", now.strftime("%p"))