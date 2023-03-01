print("program to print uppercase letters in string")
name=str(input("enter the string:"))
i =False
for c in name:
    if c.isupper():
        print(c,end=' ')
        i = True
if not i:
    print("no uppercase letters")
print("Thank You!")
