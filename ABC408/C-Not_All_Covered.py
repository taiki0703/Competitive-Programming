## N , M = map(int,input().split())

## Battery = [0] * N

## for i in range(M):
##     L , R = map(int,input().split())
##     for i in range(N):
##         if(L-1 <= i and i <= R-1):
##             Battery[i] += 1

## print(min(Battery))

## タイムエラー
## 計算量がO(MN)となり膨大
## imos法により解決する

N , M = map(int,input().split())

Battery = [0] * (N + 1)

count = [0] * (N + 1)

for i in range(M):
    L , R = map(int,input().split())
    Battery[L-1] += 1
    Battery[R] -= 1

for i in range(N + 1):
    if(i == 0):
        count[0] = Battery[0]
    if(i > 0):
        count[i] = count[i-1] + Battery[i]

count.pop(N)

print(min(count))