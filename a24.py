p = int(input("Enter price"))
r = int(input("Enter rate"))
gst = p*r/100
print(gst)
ict = int(input("Enter income tax"))
tax = gst/ict
print(tax)
