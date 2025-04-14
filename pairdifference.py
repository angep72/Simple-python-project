# Create a function that finds the pair of numbers with the smallest difference.
def smallest_difference_pair(nums):
    if len(nums) < 2:
        return None  # Not enough elements to form a pair

    nums.sort()
    min_diff = float('inf')
    closest_pair = ()

    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (nums[i], nums[i + 1])

    return closest_pair
