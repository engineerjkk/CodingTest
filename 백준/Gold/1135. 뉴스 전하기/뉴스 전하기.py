import sys 
input = sys.stdin.readline 
n=int(input())
parents=list(map(int,input().split()))

child=[[] for _ in range(n)]
for i in range(1,n):
    child[parents[i]].append(i)

def dfs(now):
    if not child[now]:
        return 0 
    times=[]
    for v in child[now]:
        times.append(1+dfs(v))
    times.sort(reverse=True)
    max_time=0
    for i,t in enumerate(times):
        max_time=max(max_time,i+t)
    return max_time
answer=dfs(0)
print(answer)