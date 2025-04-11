#Create a function that returns the longest word in a sentence.
def longest(text):
    new_arr = text.split(" ")
    new_array = []
    for num in new_arr:
       new_array.append(len(num))
    longest = new_array.index(max(new_array))
    return new_arr[longest]