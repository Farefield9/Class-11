L  = [1,5,7,9,5,5]
L.sort()
len = len(L)
if len%2 == 0:
 med=(L[len//2] + L[len//2-1])/2
else :
 med = L[len//2]
print("Median of given list is : ", med)
