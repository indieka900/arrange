x = int(input("Enter pin: "))
count = 0
while (x > 0):
    count = count + 1
    if count == 4:
        print("Sent")
    else:
        print("Invalid PIN")
        print(count)
    break