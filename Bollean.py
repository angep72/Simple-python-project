set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Check if they have any common elements
has_common = not set1.isdisjoint(set2)
print(has_common)  # Output: True
