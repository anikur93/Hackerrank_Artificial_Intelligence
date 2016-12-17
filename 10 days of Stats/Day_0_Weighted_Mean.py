# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
size = int(input())
numbers = list(map(float, input().split()))
weights = list(map(float, input().split()))
p = 0
s = 0
for i in range(len(numbers)):
    p = p + numbers[i]*weights[i]
    s = s + weights[i]
result = round(p/s,1)
print(result)