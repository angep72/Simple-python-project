import random
def guessGame():
    guessed_number = random.randint(0,10)
    return guessed_number

user_attempts = input("-------please tell us how many times you want to guess-------------\n ")

number = guessGame()
i=0
while i<=int(user_attempts):
    user_input = input("please Guess the succeess number of this game ")
       
    if(int(user_input)== number):
        print ("congratulations you have guessed the number !!!!")
        break
    i = i+1
    if(i==int(user_attempts)):
        print("Sorry you have reached the maximum number of attempts. Better luck next time! ")
        print("The correct number was :", guessGame())
        break

    
    