import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    lst=list(map(str,input().split()))
    tmp=''
    for i in range(len(lst)-1):
        tmp+=lst[i][::-1]
        tmp+=' '
    tmp+=lst[-1][::-1]
    print(tmp)