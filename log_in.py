pwd = []
user = input("Enter your user name: ")
password = input("Enter the password to create the account ")
pass1 = input("Confirm your password ")
if pass1 == password:
    pwd.append(pass1)
    print("Account created succesfully")
else:
    print("Your pasword didn't match")
person = int(input("1. Log in\n2. Change password"))
if person == 1:
    user1 = input("Enter your user name: ")
    password = input("Enter the password to create the account ")
    if password == pwd and user == user1:
        print("Log in succesfully")
    else:
        print("Incorrect log in details")
elif person == 2:
    pwd.clear()
    user1 = input("Enter your user name: ")
    if user == user1:
        pass2 = input("Enter your new password ")
        pass3 = input("Confirm your new password: ")
        if pass3 == pass2:
            print("Password changed succesfull")
            pwd.append(pass3)
        else:
            print("Your password didn't match")
    else:
        print("Your username is incorrect")
else:
    print("Invalid choice")