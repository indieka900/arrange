x = int(input("Enter pin: "))
count = 0
while (x > 0):
    count = count + 1
    x = x // 10
if count == 4:
    True
    print("Sent")
else:
    False
    print("Invalid PIN")
