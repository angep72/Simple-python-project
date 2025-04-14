# write a function that return a list on numbers each one squared
def square_numbers(number):
    return list(map(lambda x: x ** 2, number))

print(square_numbers([1,2,3,4,5]))