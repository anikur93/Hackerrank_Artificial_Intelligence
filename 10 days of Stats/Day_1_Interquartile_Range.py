size = int(input())
numbers = list(map(int, input().split()))
freq = list(map(int, input().split()))
l = []
for i in range(len(numbers)):
    for j in range(freq[i]):
        l.extend([numbers[i]])

l = sorted(l)



def divide(numbers):
    if len(numbers) % 2 == 0:
        return numbers[:(len(numbers)//2)], numbers[(len(numbers)//2) :]
    else:
        return numbers[:len(numbers)//2], numbers[(len(numbers)//2)+1 :]
    
def median(numbers):
    if len(numbers) % 2 == 0:
        return ((numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1])/2)
    else :
        return numbers[len(numbers)//2]
    
q1 = median(divide(l)[0])
q3 = median(divide(l)[1])


result = round((q3-q1) * 1.0,1)
print(result)
