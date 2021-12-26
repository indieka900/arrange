
amount = 192000
while True:
    print("Welcome to our services")
    print("1. Safaricom\n2. M-pesa\n00. Exit")
    m = int(input("Choose your option: "))
    if m == 1:
        print("1. My Account\n2. M-Banking Services")
    elif m == 2:
        print("1. Send Money\n2. Withdraw Cash\n3. "
              "Buy Airtime\n4. Loans and Savings\n5. Lipa na M-Pesa\n6. My Account")
        n = int(input("Choose your option: "))
        if n == 1:
            print("1. Enter the number\n2. Search the phone number")
            j = int(input("Choose your option: "))
            if j == 1:
                num = (input("Enter the number: "))
                if len(num) == 10:
                    a = int(input("Enter amount: "))
                    import pin2
                    if pin2 is True:
                        print("You have sent Ksh",str(a),"to",num,"your balance is",str(amount-a))
                    break
                else:
                    print("Your number is invalid")
            elif j == 2:
                name = input("Enter the name: ")
                a = int(input("Enter amount: "))
                import pin2
                if pin2 is True:
                    print("You have sent Ksh",str(a),"to",name,"your balance is ksh",str(amount-a))
                break
            else:
                print("Invalid")
        elif n == 2:
            k = int(input(("1. From ATM\n2. From AGENT")))
            if k == 1:
                agent = int(input("Enter The ATM number: "))
                a = int(input("Enter amount: "))
                import pin2
                if pin2 is True:
                    print("You have withdraw ksh",str(a),"from",agent)
                else:
                    break
        else:
            print("Thanks for visiting us")
            break
    elif m == 00:
        print("Thank you for visiting services")
        break
    else:
        print("invalid")
