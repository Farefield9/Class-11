try:
    a = int(input('Enter a number:'))
    b = int(input('Enter a number:'))
    c = a+b
    print(c)
    f = a/b
    print(f)
except ValueError:
    print('Enter int value only')
    a = 0
    b = 0
except ZeroDivisionError:
    print('Diviion by 0 not possible')
else:
    print('success')
finally:    
    d = a-b
    print(d)
    e = a*b
    print(e)
