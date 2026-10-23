username=input("Enter username   :  ")
password=input("Enter password   :")
if username=="admin":
    if password=="1234":
        print("Login sucessful")
else:
    print("Incorrect password")
    print("Username not found")        
