import sys 
input = sys.stdin.readline 

n=int(input())
arr=list(map(int,input().split()))

dp1=[arr[0]]*n
dp2=[arr[-1]]*n 

for i in range(1,n):
    dp1[i]=max(arr[i],dp1[i-1]+arr[i])

for i in range(n-2,-1,-1):
    dp2[i]=max(arr[i],dp2[i+1]+arr[i])

answer=max(dp1)

for i in range(1,n-1):
    answer=max(answer,dp1[i-1]+dp2[i+1])
print(answer)