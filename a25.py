a = float(input("Enter amount"))
p = float(input("Enter period"))
r = float(input("Enter rate"))
interest = a*p*r/100
total = a+interest
emi = total/(p*12)
print("EMI is ",emi)
