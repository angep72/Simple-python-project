def closest_to_zero(numbers):
    return min(numbers, key=abs)
nums = [3, -1, -2, 5, -0.5]
closest = closest_to_zero(nums)
print(closest)
