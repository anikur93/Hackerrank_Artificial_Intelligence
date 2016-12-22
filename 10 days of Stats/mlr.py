from sklearn import linear_model
m, n = map(int, input().split())
X = [[0 for i in range(m)] for i in range(n)] 
Y = []
for i in range(n):
    row = list(map(float, input().split()))
    Y.append(row[-1]) 
    for k in range(m):
        X[i][k] = row[k]
        
q = int(input())
Q = [[0 for i in range(m)] for i in range(q)]

for i in range(q):
    row = list(map(float, input().split()))
    for v in range(m):
        Q[i][v] = row[v]
lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for k in range(m-1):
    for i in range(q):
        ans = a + Q[i][k] * b[0] + Q[i][k+1] * b[1]
        print(round(ans, 2))