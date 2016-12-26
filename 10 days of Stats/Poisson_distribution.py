mean = float(input())
n = int(input())
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))
numerator = (2.718281**(-mean))*(mean**n)
denomenator = fact(n)
result = round(numerator/denomenator,3)
print(result)