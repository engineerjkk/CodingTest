import sys
input = sys.stdin.readline

tmp=100000
n=int(input())

answer=[]
for i in range(1,tmp):#기억
    for j in range(i,tmp):#현재
        a=j**2-i**2
        if a>n or a<0:
            break
        if a==n:
            answer.append(j)
if len(answer)>0:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)