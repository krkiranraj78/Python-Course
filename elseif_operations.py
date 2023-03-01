print("program to execute expressions")
x=int(input("enter the first value:"))
y=int(input("enter the second value:"))
ope=input("enter the operation:")
if ope=="+":
    print(x+y)
elif ope=="-":
    print(x-y)
elif ope=="/":
    print(x/y)
elif ope=="*":
    print(x*y)
else:
    print("invalid operation entered")
print("All operations are done")
print("Thank You!")