#Use string methods to extract the domain from an email.
def extract_domain (string):
    new_arr = string.split("@")
    return new_arr[0]
