N= int(input())
A = list(map(int,input().split()))
x = 0

for i in range(1,N+1):
    counter = 0
    for j in range(1,N+1):
        if(A[j-1] >= i):
            print(counter)
            counter += 1
    if(counter >= i):
        x = i

print(x)