#Login 

username=input("User Name:")
password=int(input("Password:"))
if username == "priya":
    if password == 12345:
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("User not found")