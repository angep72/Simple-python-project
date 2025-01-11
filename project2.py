#guessing the dice
import random
def roll():
    min_value = 1
    max_value = 6
    number1= random.randint (min_value, max_value)
    number2= random.randint (min_value, max_value)
    result = input("do you want to roll ")
    answer = result.lower() == "yes"
    count = input("how many times do you want to roll")
    count = int(count)
    for i in range(0,count):
       
     
   

print(roll())
