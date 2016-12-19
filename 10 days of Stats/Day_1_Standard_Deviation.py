size = int(input())
numbers = list(map(float, input().split()))
mean = sum(numbers)/len(numbers)
s = 0
for i in range(len(numbers)):
    s = s + (numbers[i] - mean)**2
result = (s/len(numbers))**0.5
result = round(result,1)
print(result)