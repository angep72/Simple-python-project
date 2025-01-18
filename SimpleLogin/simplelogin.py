def read_credentials():
    with open('login.txt', 'r') as f:
        content = f.readlines()
        new_contents=[]
        for line in content:
            user=line.split(",")
            user[1] = user[1].rstrip()
            new_contents.append(user)          
        print(new_contents)
print(read_credentials())  
    