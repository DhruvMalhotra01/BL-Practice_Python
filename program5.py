colors = ["Red","Green","Pink","Blue","Black","Purple","Yellow","Magenta","Brown"]

indexes_to_remove = {0, 2, 5}

revised_colors = [
    color
    for index, color in enumerate(colors)
    if index not in indexes_to_remove
]

print(f"Colors List: {colors}")
print(f"List After Removing Particular Elements: {revised_colors}")