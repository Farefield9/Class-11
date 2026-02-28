a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = a+b
print(c)
f = a/b
print(f)
d = a-b
print(d)
e = a*b
print(e)
try:
    f = a/b
    print(f)
except:
    print('Division by 0 Not Possible')
