# write function to search the second largest number in list
def largest(nums):
    result = sorted (nums)
    return result[len(result)-2]
