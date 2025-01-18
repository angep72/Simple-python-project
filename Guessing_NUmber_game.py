import random
def guessGame():
    guessed_number = 2
    return guessed_number

user_attempts = input("please tell us how many times you want to guess")

number = guessGame()
i=0
while i< int(user_attempts):
    user_input = input("please Guess the succeess number of this game ")
       
    if(int(user_input)== number):
        print ("congratulations you have guessed the number !!!!")
        break
    i = i+1
    