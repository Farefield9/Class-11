p = 2
r = 5
t = 1
simint = (p*r*t)/100
compint = p*((1+r/100)**t)-1
print(simint,compint)
emi = (p*r*(1+r)*t)/(((1+r)*t)-1)
print(emi)
