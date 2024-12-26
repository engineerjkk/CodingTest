import sys
input = sys.stdin.readline

n,k=map(int,input().split())

lst=list(map(str,input().strip()))
visit=[False]*n

cnt=0
for i in range(n):
    if lst[i]=='P':
        start=max(0,i-k)
        end=min(i+k,n-1)
        for j in range(start,end+1):
            if visit[j]==False and lst[j]=='H':
                visit[j]=True
                cnt+=1
                break
print(cnt)

