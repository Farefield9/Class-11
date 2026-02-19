num = int (input ("Enter the number :- "))
a = 0
b = 1
c = 0
print (0, end = " ")
while 0 < num :
    a, b = b, c
    c = b + a
    num -= 1
    print (c, end = " ")
