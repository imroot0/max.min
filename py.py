print ("""***----*** Taking three numbers from the input and displaying the largest number ***-----***""")
num1 = int(input("enter number one: "))
num2 = int(input("enter number two:"))
num3 = int(input("inter number tree: "))

if num1 > num2:
    print("max ",num1)
    if num2 > num3:
        print("min",num3)
    elif num2 < num3:
        print("min",num2)
    else:
        print("on two no tree")
    
elif num2 > num3:
    print("max",num2)
    if num1 > num3:
        print("min", num3)
    elif num1 < num3:
        print("min",num1)
    else:
        print("no 1 no 3")
    
elif num3 > num1:
    print("max", num3)
    if num1 > num2:
        print("min",num2)
    elif num1 < num2:
        print("min", num1)
    else:
        print("no 1 no 2")
        
else:
    print("on no no")