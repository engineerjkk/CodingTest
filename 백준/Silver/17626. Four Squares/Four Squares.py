import sys
input = sys.stdin.readline
n=int(input())
dp=[4]*(n+1)

for i in range(1,n+1):
    if (i**0.5).is_integer():
        dp[i]=1
        continue
    for j in range(1,n):
        if j*j>i:
            break
        dp[i]=min(dp[i],1+dp[i-j*j])

print(dp[n])