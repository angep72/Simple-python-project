#Write a function to rotate a list n positions.
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]