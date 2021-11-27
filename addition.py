j =0
print('The numbers are: ',end=' ')
for i in range(1,20+1):
    if i%2 == 0:
        j = i+j
        print(i,end=' ')
    else:
        continue
print("\nThe sum is "+str(j))