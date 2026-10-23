age=int(input("Enter age:"     ))
if age>=21:
    experience=int(input("Enter years of experience:"))
if experience>=2:
    degree=input("Do you have the required degree?(yes/no):")
if degree=="yes":
    print("Eligible for the job")
else:
    print("Required degree not available")
    print("Insufficient experience")
    print("Not eligible due to age")