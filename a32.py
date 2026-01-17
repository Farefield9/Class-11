l = eval(input("Enter a list"))
pl = list()
nl = list()
for i in l:
 if i > 0:
   pl.append(i)
 elif i < 0:
   nl.append(i)
print(pl, "is the list of positive numbers.")
print(nl, "is the list of negative numbers.")
