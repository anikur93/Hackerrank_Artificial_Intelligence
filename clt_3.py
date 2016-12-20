mean = 500
sd = 80/(100**0.5)
z = 1.96
a = mean - (z*sd)
b = mean + (z*sd)
print(round(a,2))
print(round(b,2))