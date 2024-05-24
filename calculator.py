x=int(input("Enter the number:"))
a=input("Enter the operator")
y=int(input("Enter the number"))
if a == "+":
    print(x+y)
elif a =="-":
    print(x-y)
elif a =="*":
    print(x*y)
elif a =="/":
    if y ==0:
        print("Error")
    else:
        print(x/y)