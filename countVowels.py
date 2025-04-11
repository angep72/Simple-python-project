# Write a function that counts the number of vowels in a string

def countvowels(strings):
    string = strings.lower()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for s in vowels:
        if s in vowels:
            count += 1

    return f"we have found {count} vowels"


