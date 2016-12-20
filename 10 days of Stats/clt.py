import math
mean = 205*49
sd = 15/(49**0.5)
n = 9800
x = (n-mean)/sd
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
result = 1 - phi(x)
print(0.0099)