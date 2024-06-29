import heapq
import sys
input = sys.stdin.readline
n=int(input())
a=-int(input())
if n==1:
    print(0)
    exit()
lst=[]
for _ in range(n-1):
    heapq.heappush(lst,-int(input()))
ans=0
while True:
    if a<lst[0]:
        break
    b=heapq.heappop(lst)
    b+=1
    heapq.heappush(lst,b)
    a-=1
    ans+=1
print(ans)
