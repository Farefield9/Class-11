a = input("Enter any string")
ch = input("Enter the alphabet")
count = 0
for i in a:
    if ch==i:
        count = count+1
print(ch,"occurs",count,"times in ",a)
