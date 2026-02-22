# insertion sort
l = eval(input("enter list"))
for i in range(1,len(l)): #i = no. of elements in a list
    a = l[i]
    j=i-1
    while j>=0 and a < l[j]:
        l[j+1] = l[j]
        j=j-1
    else:
        l[j+1] = a
print(l)
