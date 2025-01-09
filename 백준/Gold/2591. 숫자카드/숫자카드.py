import sys 
input = sys.stdin.readline 

numbers=input().strip()
n=len(numbers)

dp=[0]*(n+1)
dp[0]=1

for i in range(n):
    if numbers[i]!='0':
        dp[i+1]+=dp[i]
    
    if i>0 and dp[i-1]!='0':
        num=int(numbers[i-1:i+1])
        if 10<=num<=34:
            dp[i+1]+=dp[i-1]
print(dp[n])