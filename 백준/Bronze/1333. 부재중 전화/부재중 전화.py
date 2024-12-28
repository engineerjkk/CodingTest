import sys
input = sys.stdin.readline

N,L,D=map(int,input().split())

check=[False]*5000

idx=0
for _ in range(N):
    for _ in range(L):
        check[idx]=True
        idx+=1
    for _ in range(5):
        idx+=1

for i in range(0,5000,D):
    if not check[i]:
        print(i)
        break
  