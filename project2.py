import random
def roll():
    min_value = 1
    max_value = 6
    number1= random.randint (min_value, max_value)
    number2= random.randint (min_value, max_value)
    return number1, number2

print(roll())
