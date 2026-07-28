import datetime

date_string = "27 Jul 2026"

print("Date as Date String:", date_string)
print(type(date_string))

date_object = datetime.datetime.strptime(date_string, "%d %b %Y")

print()
print("Date as DateTime object:", date_object)
print(type(date_object))