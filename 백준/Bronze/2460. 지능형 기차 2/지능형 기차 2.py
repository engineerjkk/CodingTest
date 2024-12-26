import sys
input= sys.stdin.readline
answer=0
total=0
for _ in range(10):
    op,ip=map(int,input().split())
    total-=op
    total+=ip
    answer=max(answer,total)
print(answer)