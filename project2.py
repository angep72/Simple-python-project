#this is the progrma that allows the user to keep on saying whether they want to continue playing the game or not once it is not it will end saying game over
import random
def roll():
    min_value = 1
    max_value = 6
    number1= random.randint (min_value, max_value)
    number2= random.randint (min_value, max_value)
    return number1, number2  # return a tuple of two dice values
def generate_rolling():
    print("-------------Welcome to the dice rolling game!!!!------------")
    counts = input("how many times do you want to place the dice")
    i=0
    while i < int(counts):
         userInput= input("do you want to roll")
         while userInput.lower() == "yes":
            dice1, dice2 = roll()
            print(f"You rolled: {dice1} and {dice2}")
            userInput = input("Do you want to roll again?")
            if userInput.lower() == "no":
                break
            print("Thanks for playing!")

    
generate_rolling()
    
