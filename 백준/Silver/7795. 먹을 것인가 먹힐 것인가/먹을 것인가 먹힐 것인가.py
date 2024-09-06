import sys
input = sys.stdin.readline
t=int(input())
answer=[]
for _ in range(t):
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    main=0
    sub=0
    ans=0
    while main<n:
        if sub==m:
            ans+=sub
            main+=1
        elif A[main]<=B[sub]:
            ans+=sub
            main+=1
        else:
            sub+=1
    answer.append(ans)
for i in answer:
    print(i)