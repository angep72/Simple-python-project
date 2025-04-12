#write a function to change a word into snake case
def snake_case(string):
    result = string.strip().lower()
    snake_array = result.split(" ")
    return "_".join(snake_array)


