# Count the frequency of words in a sentence using a dictionary.

sentence = ("Hello world how have you been world")
new_sentence = sentence.split(" ")
new_obj = {}
for word in new_sentence:
    if word in new_obj:
        new_obj[word] += 1
    else:
        new_obj[word] = 1
print(new_obj)