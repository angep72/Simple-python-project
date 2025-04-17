# #people = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("Diana", 25)]
# grouped = group_by_age(people)
# print(grouped)
# {30: ['Alice', 'Charlie'], 25: ['Bob', 'Diana']}


def print_person(people):
    age_groups = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        if age not in age_groups:
            age_groups[age] = []
        age_groups[age].append(name)
    return age_groups

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 25}
]
grouped = print_person(people)
print(grouped)
