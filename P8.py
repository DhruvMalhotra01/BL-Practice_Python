from datetime import date, timedelta

# Today's date
today = date.today()

# Days until next Monday
days_until_monday = (7 - today.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7

# Fellowship starts next Monday
start_date = today + timedelta(days=days_until_monday)

# Fellowship duration = 12 weeks
completion_date = start_date + timedelta(weeks=12)

print("Fellowship start date:", start_date)
print("Fellowship completion date:", completion_date)