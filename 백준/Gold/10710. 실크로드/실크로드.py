import sys 
input = sys.stdin.readline 

n,m=map(int,input().split())
D=[]
for _ in range(n):
    D.append(int(input()))
C=[]
for _ in range(m):
    C.append(int(input()))

dp=[[1e9]*(n+1) for _ in range(m+1)]
dp[0][0]=0

for i in range(m):
    for j in range(n+1):
        if dp[i][j]==1e9:
            continue 

        dp[i+1][j]=min(dp[i+1][j],dp[i][j])

        if j<n:
            next_fatigue=dp[i][j]+D[j]*C[i]
            dp[i+1][j+1]=min(dp[i+1][j+1],next_fatigue)

result=1e9
for i in range(1,m+1):
    result=min(result,dp[i][n])
print(result)
