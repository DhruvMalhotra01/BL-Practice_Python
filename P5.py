school_friends = ["John", "Alice", "Bob", "David"]
college_friends = ["Alice", "Charlie", "David", "Eve"]

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find all unique friends using | operator
all_friends = set(school_friends) | set(college_friends)

# Display result
print("\nAll friends (Set | operator):", list(all_friends))