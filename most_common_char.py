def word(s):
    new_obj = {}
    for char in s:
        if char in new_obj:
            new_obj[char] += 1
        else:
            new_obj[char] = 1

    new_arr = list(new_obj.values())

    for i in new_obj:
        if new_obj[i] == max(new_arr):
            return i
    print(new_obj)


