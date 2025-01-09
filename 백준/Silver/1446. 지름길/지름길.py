import sys 
input = sys.stdin.readline 

n,d=map(int,input().split())
shortcuts=[]
for _ in range(n):
    shortcuts.append(list(map(int,input().split())))

dp=[]
for i in range(d+1):
    dp.append(i)

for i in range(1,d+1):
    
    dp[i]=min(dp[i],dp[i-1]+1)
    
    for start,end,length in shortcuts:
        if i==end and start<=end and end<=d:
            dp[i]=min(dp[i],dp[start]+length)
print(dp[d])