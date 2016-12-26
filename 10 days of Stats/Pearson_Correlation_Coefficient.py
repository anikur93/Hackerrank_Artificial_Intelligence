size = int(input())
numbers1 = list(map(float, input().split()))
numbers2 = list(map(float, input().split()))
mean1 = sum(numbers1)/len(numbers1)
mean2 = sum(numbers2)/len(numbers2)
s = 0
for i in range(len(numbers1)):
    s = s + (numbers1[i] - mean1)**2
sd1 = (s/len(numbers1))**0.5

s2 = 0
for i in range(len(numbers2)):
    s2 = s2 + (numbers2[i] - mean2)**2
sd2 = (s2/len(numbers2))**0.5

s3 = 0
for i in range(len(numbers2)):
    s3 = s3 + ((numbers1[i]-mean1)*(numbers2[i]-mean2))
per = (s3/(len(numbers2)*sd1*sd2))
per = round(per,3)
print(per)
