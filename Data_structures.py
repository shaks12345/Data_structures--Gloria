my_list = []

# Append elements 10, 20, 30, 40 to the list
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30
index = my_list.index(30)

# Print the index
print(f"The index of 30 in the list is: {index}")

# Print the final list (optional)
print(my_list)
