import sys
input = sys.stdin.readline
n = int(input())
dp=[4]*(n+1)
dp[0]=0
for i in range(1,n+1):
    if (i**0.5).is_integer():
        dp[i]=1
    for j in range(n):
        if j*j>i:
            break
        dp[i]=min(dp[i],1+dp[i-j*j])
print(dp[n])
