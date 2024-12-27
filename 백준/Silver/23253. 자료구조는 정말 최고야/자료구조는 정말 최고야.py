import sys
input = sys.stdin.readline
n,m=map(int,input().split())

flag=True
for _ in range(m):
    k=int(input())
    a=list(map(int,input().split()))

    for i in range(1,len(a)):
        if a[i-1]<a[i]:
            flag=False
            break
if flag:
    print("Yes")
else:
    print("No")