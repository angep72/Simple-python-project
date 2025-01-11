import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

value = roll()

while True:
    players = input('Please enter the number of players (1-4): ')
    
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1 and 4.")
    else:
        print("Invalid input. Please enter a number.")

print(f"Number of players: {players}")
