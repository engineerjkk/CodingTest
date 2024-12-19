import sys
input = sys.stdin.readline


def solution(k,coins):
    dp=[0]*(k+1)
    dp[0]=1

    for coin in coins:
        for i in range(coin,k+1):
            dp[i]+=dp[i-coin]
    return dp[k]

n,k=map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))
print(solution(k,coins))