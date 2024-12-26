import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
cnt=0
answer=0
for i in range(n):
    if lst[i]==1:
        cnt+=1
        answer+=cnt
    else:
        cnt=0
print(answer)