import sys 
input = sys.stdin.readline 

a,b,c=map(int,input().split())

s1=list(range(1,a+1))
s2=list(range(1,b+1))
s3=list(range(1,c+1))

cnt=[0]*(a+b+c+1)
for i in s1:
    for j in s2:
        for k in s3:
            cnt[i+j+k]+=1
answer=0
result=0
for i in range(1,len(cnt)):
    if answer<cnt[i]:
        answer=cnt[i]
        result=i

    
print(result)