school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find common friends using iteration
common_friends = []
for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)

# Display common friends
print("\nCommon friends (Iterative method):", common_friends)