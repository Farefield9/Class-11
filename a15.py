list = [1,5,8,4,31,45]
choice = 0
for attempt in range(3) :
    print("Attempt Number:",attempt)
print("The list has the following element",list)
print("L I S T   O P E R A T I O N S")
print("1.Append an element")
print("2.Insert an element")
print("3.Append a list to the given list")
print("4.Modify an existing element")
print("5.delete an existing element from its position")
print("6.Delete an existing element with a given value")
print("7.sort the list in ascending order")
print("8.sort the list in descending order")
print("9.Display the list")
choice = int(input("Enter the choice from 1-9:"))

if choice == 1:
    element = eval(input("Enter the element to be appended"))
    list.append(element)
    print("The element has been appended")
list =[]
print("How many students marks you want to enter:")
n = int(input())
for i in range(0,n):
    print("Enter marks of student",(i+1),":")
    marks = int(input())
    list.append(marks)
    total = 0
    for marks in list:
        total = total  + marks
        average = total/n
        print("average marks of",n,"student is ",average)
st = input("Enter a string:")
dic = {}
for i in st:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        for key in dic :
                print(key ,":",dic[key])
num = input("Enter a number:")
dic = {'1':'one','2' :'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
for i in num :
    print(dic[i],end = '')
for i in dic:
    print(dic[i])
list = eval(input("Enter a list"))
element  = eval(input("Enter the element to be searched"))
leng = len(list)
count= 0
for i in range(leng):
    if element == list[i]:
        count +=1
if count == 0:
    print(element,"not found")
else:
    print(element,"come",count,"time")
st = eval(input("Enter list:"))
sortedlist = sorted(st)
print("l1:",sortedlist[-1])
print("l2",sortedlist[-2])
a = eval(input("Enter a list:"))
newlist = []
for i in a:
    if i not in newlist:
        newlist.append(i)
        a = newlist
        print("list :",a)
x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
z = int(input("Enter a number:"))
if (x<y and y<z):
    print(x,"<",y,"<",z)
elif (x<z and z<y):
    print(x,"<",z,"<",y)
elif(y<x and x<z):
    print(y,"<",x,"<",z)
elif(y<z and z<x):
    print(y,"<",z,"<",x)
elif(z<x and x<y):
    print(z,"<",x,"<",y)
else:
    print(z,"<",y,"<",x)
