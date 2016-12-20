import math
mean = 2.4
sd = 2/(100**0.5)
n= 250/100
x = (n-mean)/sd
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

result =phi(x)
print(round(result,4))