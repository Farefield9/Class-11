a = eval(input("Enter a list"))
n = []
for i in a :
    if i not in n:
        n.append(i)
        a = n
print("l",a)
