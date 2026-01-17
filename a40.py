text = 'w3source'
dict = {}
index = 0
for i in text:
    if i not in dict:
        dict[i] = index
        index = index+1
print(dict)
