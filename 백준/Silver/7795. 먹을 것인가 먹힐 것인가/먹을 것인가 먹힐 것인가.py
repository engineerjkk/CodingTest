import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    lst_n=list(map(int,input().split()))
    lst_m=list(map(int,input().split()))
    lst_n.sort()
    lst_m.sort()
    sub=0
    main=0
    cnt=0
    while main<n:
        if sub==m:
            cnt+=sub
            main+=1
        else:
            if lst_n[main]<=lst_m[sub]:
                cnt+=sub
                main+=1
            else:
                sub+=1
    print(cnt)
