N = int(input())
T = list(input())
A = list(input())

areWanted = False

for i in range(N):
    if(T[i] == "o" and A[i] == "o"):
        areWanted = True
        break

if(areWanted == True):
    print("Yes")
else:
    print("No")