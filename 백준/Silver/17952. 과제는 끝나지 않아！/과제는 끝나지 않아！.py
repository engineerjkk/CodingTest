import sys
input = sys.stdin.readline
n=int(input())

stack=[]
score=0
for _ in range(n):
    info=list(map(int,input().split()))
    if info[0]==0:
        if len(stack)!=0:
            a,t=stack.pop()
            if t==1:
                score+=a
            else:
                stack.append((a,t-1))
    if info[0]==1:
        a=info[1]
        t=info[2]
        if t==1:
            score+=a
        else:
            stack.append((a,t-1))
print(score)