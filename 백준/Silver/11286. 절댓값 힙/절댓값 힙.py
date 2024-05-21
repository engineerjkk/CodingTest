import sys
input = sys.stdin.readline
import heapq

n = int(input())
lst=[]
for _ in range(n):
    a=int(input())
    lst.append(a)


ans=[]

for i in range(n):
    if lst[i]!=0:
        heapq.heappush(ans,(abs(lst[i]),lst[i]))
    else:
        if len(ans)!=0:
            print(heapq.heappop(ans)[1])
        else:
            print(0)

        