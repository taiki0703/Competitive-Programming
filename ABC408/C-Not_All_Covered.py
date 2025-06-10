N , M = map(int,input().split())

Battery = [0] * N

for i in range(M):
    L , R = map(int,input().split())
    for i in range(N):
        if(L-1 <= i and i <= R-1):
            Battery[i] += 1

print(min(Battery))

##タイムエラー