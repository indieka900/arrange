for i in range(0,4):
    pin = input("Enter the pin: ")
    l = len(pin)
    if l == 4:
        print("Correct!")
        break
else:
    print("Invalid!")
    pass