size = int(input())
numbers1 = list(map(float, input().split()))
numbers2 = list(map(float, input().split()))
numbers11 = sorted(numbers1)
numbers22 = sorted(numbers2)
rankx = [numbers11.index(k)+1 for k in numbers1]
ranky = [numbers22.index(k)+1 for k in numbers2]
diff = [x1 - x2 for (x1, x2) in zip(rankx, ranky)]
dd = [x1*x2 for (x1, x2) in zip(diff,diff)]
d = sum(dd)
r = 1 - ((6*d)/(((size**2) - 1)*size))
print(round(r,3))