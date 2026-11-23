N = int(input())
A = list(map(int,input().split()))

A.sort()

pop = []

for i in range(1,N):
    if(A[i] == A[i-1]):
        pop.append(i)

for i in range(len(pop)):
    A.pop(pop[i] - i)        
        

print(len(A))
for i in range(len(A)):
    print(A[i])
