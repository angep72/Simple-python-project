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
    for user in credintials:
        print(user)
        
    
print(login_names("ange","ange123"))  
    