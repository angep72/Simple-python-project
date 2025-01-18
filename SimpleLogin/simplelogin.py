def read_credentials():
    with open('login.txt', 'r') as f:
        content = f.readlines()
        new_contents=[]
        for line in content:
            user=line.split(",")
            user[1] = user[1].rstrip()
            new_contents.append(user)          
        return(new_contents)
    
def login_names(name,password):
    credintials = read_credentials()
    logged_in = False
    for user in credintials:
        if user[0] == name and logged_in == False:
            if user[1] == password:
                logged_in = True
    
    if logged_in == True:
        return "Login Successful"
    else:
        return "Login Failed"
        
    
def main ():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    result = login_names(name, password)
    print(result)  
    
main()
    