#Remove all odd numbers from a list.
def removeodd(num):
    result = []
    for i in num:
        if i % 2 != 0:
            result.append(i)
    return result
