import sys
input = sys.stdin.readline
t=int(input())
answer=[]
for _ in range(t):
    n,m=map(int,input().split())
    lst_n=sorted(list(map(int,input().split())))
    lst_m=sorted(list(map(int,input().split())))
    cnt=0
    main=0
    sub=0
    while main<n:
        if sub==m:
            cnt+=sub
            main+=1
        else:
            if lst_n[main]<=lst_m[sub]:
                main+=1
                cnt+=sub
            else:
                sub+=1
    answer.append(cnt)
for i in answer:
    print(i)
