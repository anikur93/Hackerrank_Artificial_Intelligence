x1,y1 = list(map(int, input().split()))
x2,y2 = list(map(int, input().split()))
x3,y3 = list(map(int, input().split()))
x4,y4 = list(map(int, input().split()))
x5,y5 = list(map(int, input().split()))
sumx = x1 + x2 + x3 + x4 + x5
sumy = y1 + y2 + y3 + y4 + y5
sumxy = x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5
sumx2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2
sumy2 = y1**2 + y2**2 + y3**2 + y4**2 + y5**2

a = ((sumy * sumx2) - (sumx * sumxy))/((5*sumx2)-sumx**2)
b = ((5 * sumxy) - (sumx*sumy))/((5*sumx2)-sumx**2)

y = a + b * 80
print(round(y,3))