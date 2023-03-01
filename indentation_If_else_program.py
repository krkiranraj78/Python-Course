print("program to understand indentations")
age=int(input("enter your age:"))
#age=int(age)
if age > 18:
    print("you are an adult, you can vote")
    print("enjoy your rights")
    if age>60:
        print("You are a senior citizen")
    else:
        print("you are not a senior citizen")
elif age<18 and age>16:
    print("you are not an adult, but a teenager")
else:
    print("you are a child")
print("Thank You!")
