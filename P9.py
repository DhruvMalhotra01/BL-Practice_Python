access_rights = input("Enter the employees with access rights (comma-separated): ")
current_employees = input("Enter the current employees (comma-separated): ")

# Convert input into sets (case-insensitive)
access_set = {employee.strip().lower() for employee in access_rights.split(",")}
current_set = {employee.strip().lower() for employee in current_employees.split(",")}

# Update access rights using intersection_update()
access_set.intersection_update(current_set)

# Display updated access rights
print("\nUpdated Access Rights List:")

for employee in access_set:
    print(employee.title())