import math
a = (80 - 70)/10
b = (60 - 70)/10

def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

result1 = (1-phi(a))*100
result1 = round(result1,2)
result2 = (1-phi(b))*100
result2 = round(result2,2)
result3 = phi(b)*100
result3 = round(result3,2)
print(result1)
print(result2)
print(result3)