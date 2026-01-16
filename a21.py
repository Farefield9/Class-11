x = int(input("Enter the number"))
print("The factor of",x,"is:")
for i in range(1,x+1):
    if (x%i)==0:
        print(i)
