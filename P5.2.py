school_friends = ["John", "Alice", "Bob", "David"]
college_friends = ["Alice", "Charlie", "David", "Eve"]

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find all unique friends using union() method
all_friends = set(school_friends).union(college_friends)

# Display result
print("\nAll friends (Set union method):", list(all_friends))