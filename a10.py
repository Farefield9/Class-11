a = [1,5,2,4,8,9,6,7,3,5,24]
for i in a:
    if (i%2) == 0:
        print(i,"is even")
for i in range(-3,10,2):
    if i < 0:
        print(i+1)
    else:
        print(i)
for d in range (4):
    print(d)
for var1 in range(3):
    print("iteration" + str(var1 +1) + "of outer loop")
    for var2 in range(2):
        print(var2 + 1)
        print("out of inner loop")
        print("out of outer loop")
