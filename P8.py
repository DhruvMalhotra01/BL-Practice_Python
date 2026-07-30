current_emails = input("Enter the current subscribers' emails (comma-separated): ")
new_emails = input("Enter the new sign-ups' emails (comma-separated): ")

# Convert input into sets
current_set = {email.strip().lower() for email in current_emails.split(",")}
new_set = {email.strip().lower() for email in new_emails.split(",")}

# Check for common email addresses
if current_set.isdisjoint(new_set):
    print("There are no common email addresses between current subscribers and new sign-ups.")
else:
    common_emails = current_set.intersection(new_set)

    print("The following email addresses are present in both lists:")
    for email in common_emails:
        print(email)