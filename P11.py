import calendar

month = int(input("Enter the month (1-12) : "))
year = int(input("Enter the year (Ex. 2026) : "))

print()
print(calendar.month_name[month], year)

month_calendar = calendar.monthcalendar(year, month)

print("Mo Tu We Th Fr Sa Su")

for week in month_calendar:
    for day in week:
        if day == 0:
            print("   ", end="")
        else:
            print(f"{day:2}", end=" ")
    print()