import sys
input = sys.stdin.readline

n,l,d=map(int,input().split())
MAX=20*185

check=[False]*MAX


idx=0
for _ in range(n):
    for _ in range(l):
        check[idx]=True
        idx+=1
    for _ in range(5):
        idx+=1

for i in range(0,MAX,d):
    if not check[i]:
        print(i)
        break