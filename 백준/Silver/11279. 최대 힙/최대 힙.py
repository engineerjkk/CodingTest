import sys
input = sys.stdin.readline
import heapq
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

ans=[]
for i in range(n):
    a=lst[i]
    if a!=0:
        heapq.heappush(ans,-a)
    else:
        if len(ans)==0:
            print(0)
        else:
            print(-heapq.heappop(ans))

