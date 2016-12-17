# -*- coding: utf-8 -*-
size = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)

def median(numbers):
    if len(numbers) % 2 == 0:
        return ((numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1])/2)
    else :
        return numbers[len(numbers)//2]

def divide(numbers):
    if len(numbers) % 2 == 0:
        return numbers[:(len(numbers)//2)], numbers[(len(numbers)//2) :]
    else:
        return numbers[:len(numbers)//2], numbers[(len(numbers)//2)+1 :]
    
q1 = median(divide(numbers)[0])
q2 = median(numbers)
q3 = median(divide(numbers)[1])

print("%.0f" % q1)
print("%.0f" % q2)
print("%.0f" % q3)