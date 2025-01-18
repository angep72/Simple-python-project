def additon(a,b):
 return a + b

def substract (a,b):
    return a - b

first_number = input("please enter the first number ") 
second_number = input("please enter the second number ")

operation = input("which operation do you want to perform? ")

if (operation == "addition"):
    result = additon(float(first_number), float(second_number))
    print(f"The result is {result}")
elif (operation == "substraction"):
    result = substract(float(first_number), float(second_number))
    print(f"The result is {result}")
else:
    print("Invalid operation. Please choose either addition or subtraction.")


