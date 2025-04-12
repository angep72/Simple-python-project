#Write a function that returns every other character in a string..
def return_every_character(string):
    for char in range(0,len(string),2):
        print(string[char])
