N , L = map(int,input().split())
d = list(map(int,input().split()))


plot = [0] * N

for i in range(1,len(plot)):
    plot[i] = plot[i-1] + d[i-1]
    if(plot[i] >= L):
        plot[i] %= L


print(plot)
