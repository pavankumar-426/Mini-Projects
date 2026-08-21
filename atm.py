atm_pin=43124
balance=100
for i in range(5):
    print(f"only u have a {5-i} chance left")
    c=int(input("Enter the ATM pin :"))
    if c==atm_pin:
        while True:
            option=int(input("1.check balance \n2.withdraw \n3.credit \n4.Exit : \n"))
            if option==1:
                print(f"\nYour Account Balance is : ₹{balance}")
            elif option==2:
                print(f"Your Current Account balace is: ₹{balance}")
                user_amount=int(input("Enter the amount:"))
                if user_amount<=balance:
                    balance=balance-user_amount
                    print(f"withdraw sucessfully {user_amount} and Your current Account balance is :₹ {balance}")
                else:
                    print("Sorry insufficent balance")
            elif option==3:
                print(f"Your Current Account balace is: ₹{balance}")
                user_amount=int(input("Enter the amount:"))
                balance=balance+user_amount
                print(f"Amount credit Sucessfuly: {user_amount}")
                print(f"Your Current amount balance : ₹{balance}")
            elif option==4:
                print("Thanks for Using ATM services ")
                break
            else:
                print("Invalid choice")
                
    else:   
        print("Wrong ATM pin Acess detined ")
    