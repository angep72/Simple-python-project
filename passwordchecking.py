#Create a function that validates a password using string methods

def check_password(password):
    if len(password) < 8:
        return "Password must contain at least 8 characters"
    if not any(passw.isupper() for passw in password):
        return "Password must contain at least one letter which is capital"
    special_chars = "!@#$%^&*()-_+="
    if not any(char in special_chars for char in password):
        return "password should contain at least one special character"
    special_digit = "0123456789"
    if not any(digit in special_digit for digit in password):
        return "password should contain at_least one digit"
    else:
        return "congratulations for the valid password !!!"