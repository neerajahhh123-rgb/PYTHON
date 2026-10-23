a=int(input("Enter first no:  "))
b=int(input("Enter second no:  "))
op=input("Enter operator(+,-,*,/):")
if op=="+":
    print("Result=",a+b)
elif op=="-":
    print("Result=",a-b)
elif op=="*":
    print("Result=",a*b)
elif op=="/":
     print("Result=",a/b)
else:
    print("Cannot divide by zero")
