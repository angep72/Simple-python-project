# Write a function that finds all duplicate items in a list.

def findDuplicate(nums):
    new_obj = {}
    result = []
    for num in nums:
        if num in new_obj:
            new_obj[num] += 1
        else:
            new_obj[num] = 1

    for num in new_obj:
        if new_obj[num] > 1:
            result.append(num)
    return result



