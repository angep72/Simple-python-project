#Use dictionary comprehension to filter values.


my_dict = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
filtered_dict = {k: v for k, v in my_dict.items() if v > 10}
print(filtered_dict)
# Output: {'b': 15, 'd': 20}
