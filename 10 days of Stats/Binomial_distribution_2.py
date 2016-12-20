def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l = list(map(float, input().split(" ")))
result2 = round(sum([b(i, 10, 0.12) for i in range(2, 11)]), 3)
result1 = round(sum([b(i, 10, 0.12) for i in range(0, 3)]), 3)
print(result1)
print(result2)