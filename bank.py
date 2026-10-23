balance=10000
amount=int(input("Enter withdrawal amount:    "))
if amount<0:
    print("Invalid amount")
elif amount>balance:
    print("Insufficient balance")
elif amount % 100!=0:
    print("Amount must be a multiple of 100")
else:
    print("Withdrawal sucessful")