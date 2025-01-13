import sys 
input = sys.stdin.readline 

t=int(input())

for _ in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    dp=[-1e9]*n 
    dp[0]=lst[0]
    for i in range(1,n):
        dp[i]=max(lst[i],dp[i-1]+lst[i])
    print(max(dp))