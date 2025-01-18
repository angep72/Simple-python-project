import random
def guessGame():
    guessed_number = random.randint(1, 100)
    return guessed_number

user_input = input("please Guess the succeess number of this game ")

number = guessGame()
if(number == int(user_input)):

    