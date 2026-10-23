login=input("Are you loggrd in?(yes/no):     ")
if login=="yes":
    cart=int(input("Enter number of items:      "))
    if cart=="no":
        payment=input("Payment sucessful?(yes/no):    ")
    if payment=="yes":
          print("Order placed sucessfully")
else:
     print("Payment failed")
     print("Cart is empty")
     print("please login first")
                     
