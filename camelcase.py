#Convert a string to camelCase.
def camelcase(s):
    if not s:
        return ""

    words = s.split(" ")
    result = words[0] + "".join(word.capitalize() for word in words[1:])
    print (result)

