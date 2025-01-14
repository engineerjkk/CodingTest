import sys 
input = sys.stdin.readline 

t=int(input())
for _ in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    s=set(lst)

    lst.sort()
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if 2*lst[j]-lst[i] in s:
                cnt+=1 
    print(cnt)