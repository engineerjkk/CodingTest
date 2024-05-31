import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
lst_n=list(map(int,input().split()))
lst_m=list(map(int,input().split()))

MAX=max(n,m)
answer=[]
for i in range(MAX):

    if i<n:
        heapq.heappush(answer,lst_n[i])

    if i<m:
        heapq.heappush(answer,lst_m[i])

while len(answer):
    print(heapq.heappop(answer), end=" ")