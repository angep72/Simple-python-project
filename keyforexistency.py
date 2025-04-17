# Write a function to check if a key exists in a dictionary.


def keyExistence(key):
    new_obj = {
        "name":"pauline"
    }
    if key in new_obj:
        return True
    else:
        return False

print(keyExistence("name"))

