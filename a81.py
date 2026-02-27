#bubble shot
size = int(input('enter the size of list:'))
a = []
for i in range(size):
    val = int(input('enter number:'))
    a.append(val)
for i in range(size):
    for j in range(0,size-i-1):
        if a[j]>a[j+1]:
            t =a[j]
            a[j] = a[j+1]
            a[j+1] = t
print('sorted list is :')
print(a)
