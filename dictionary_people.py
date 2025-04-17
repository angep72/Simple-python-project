#people = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("Diana", 25)]
# people = [ ["Alice","bob","Charlie","Diana"],[30,25,30,25]]
# grouped = group_by_age(people)
# print(grouped)
# {30: ['Alice', 'Charlie'], 25: ['Bob', 'Diana']}


def group_by_age(people):
    age_groups = {}
    for name, age in people:
        if age not in age_groups:
            age_groups[age] = []
        age_groups[age].append(name)
    return age_groups
people = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("Diana", 25)]
grouped = group_by_age(people)
print(grouped)
