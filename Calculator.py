while True:
    a=int(input("Enter the a Value: "))
    b=int(input("Enter the a Value: "))
    option=int(input("1 +\n2 -\n3 *\n4 /\n5 //\n6 %\n7 **\n8 Exit \n"))
    if option==1:
        print("\nAdddition of  two numbers =",a+b)
    elif option==2:
        print("\n subraction of  two numbers",a-b)
    elif option==3:
        print("\n Multiplication of  two numbers",a*b)
    elif option==4:
        print("\n Division  of  two numbers",a/b)
    elif option==5:
        print("\n Floora Division two numbers",a//b)
    elif option==6:
        print("\n Modulus  of  two numbers",a%b)
    elif option==7:
        print("\n Power of  two numbers",a**b)
    elif option==8:
        print("\nExiting the Calulator")
        break
    else:
        print("\nInvalid option!")
