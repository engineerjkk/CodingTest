import sys 
input = sys.stdin.readline 

N,m,M,T,R=map(int,input().split())
initial_m=m
time=0
if initial_m+T>M:
    print(-1)
    exit()
while N>0:
    time+=1
    if m+T>M:
        m-=R
        m=max(m,initial_m)
    else:
        m+=T
        N-=1
print(time)