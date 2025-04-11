# Write a function that checks if a string is a palindrome.

def palindrome_string(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not palindrome "


