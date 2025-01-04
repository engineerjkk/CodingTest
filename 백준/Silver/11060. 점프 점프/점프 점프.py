import sys
input = sys.stdin.readline 

n=int(input())
lst=list(map(int,input().split()))

dp=[1e9]*n 
dp[0]=0

for i in range(n):

    if dp[i]==1e9:
        continue 

    for j in range(1,lst[i]+1):

        if i+j>=n:
            break
        dp[i+j]=min(dp[i+j],dp[i]+1)

if dp[n-1]==1e9:
    print(-1)
else:
    print(dp[n-1])