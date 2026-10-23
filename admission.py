entrance=int(input("Enter entrance exam mark:"   ))
if entrance>60:
    maths=int(input("Enter mathematics mark:"   ))
if maths>=50:
    english=int(input("Enter english mark:"   ))
if english>50:
    print("Adission approved")
else:
    print("Rejected due to english mark")            
    print("Rejected due to mathematics mark")
    print("Rejected due to entrance exam")