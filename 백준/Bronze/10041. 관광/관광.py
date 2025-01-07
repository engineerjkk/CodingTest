import sys 
input = sys.stdin.readline 

w,h,n=map(int,input().split())
p=[]
for _ in range(n):
    p.append(list(map(int,input().split())))

answer=0
for i in range(n-1):
    x1,y1=p[i]
    x2,y2=p[i+1]

    if x1>x2:
        x1,x2=x2,x1 
        y1,y2=y2,y1 

    if y1>y2:
        answer+=abs(x1-x2)+abs(y1-y2)
    else:
        answer+=max(abs(x1-x2),abs(y1-y2))
print(answer)