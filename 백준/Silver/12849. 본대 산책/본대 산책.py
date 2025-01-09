import sys 
input = sys.stdin.readline 
D=int(input())
mod=int(1e9+7)
graph=[[] for _ in range(8)]

edges=[
    (0,1),
    (0,2),
    (1,2),
    (1,3),
    (2,3),
    (2,4),
    (3,4),
    (3,5),
    (4,5),
    (4,6),
    (5,7),
    (6,7),
]

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

dp=[[0]*8 for _ in range(D+1)]
dp[0][0]=1

for i in range(1,D+1):
    for j in range(8):
        dp[i][j]=0
        for k in graph[j]:
            dp[i][j]+=dp[i-1][k]
            dp[i][j]%=mod 

print(dp[D][0])