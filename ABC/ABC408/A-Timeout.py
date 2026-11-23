N , S = map(int,input().split())
T = list(map(int,input().split()))

isSleep = False

for i in range(N):
    if(i == 0 and T[0] >= S + 0.5):
        isSleep = True
    if(i != 0 and T[i] - T[i-1] >= S + 0.5):
        isSleep = True

if(isSleep == True):
    print("No")
else:
    print("Yes")