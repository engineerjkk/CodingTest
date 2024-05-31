import sys
input = sys.stdin.readline
t=int(input())
answer=[]

for _ in range(t):
    n=int(input())
    lst=[]
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    lst.sort()
    MAX=sys.maxsize
    cnt=0
    for i in range(n):
        if lst[i][1]<MAX:
            cnt+=1
            MAX=min(MAX,lst[i][1])
    answer.append(cnt)
for i in answer:
    print(i)

