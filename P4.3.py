school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find common friends using the intersection() method
common_friends = list(set(school_friends).intersection(college_friends))

# Display common friends
print("\nCommon friends (Set intersection method):", common_friends)