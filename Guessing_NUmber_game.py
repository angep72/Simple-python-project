import random
def guessGame():
    guessed_number = random.randint(1, 100)
    return guessed_number

user_input = input("please Guess the succeess number of this game ")
user_attempts = input("please tell us how many times you want to guess")

number = guessGame()
i=0
while i< int(user_attempts):
    