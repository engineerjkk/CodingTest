import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

lst.sort()
flag=False
for i in range(n):
    if lst[i]!=(i+1):
        print(i+1)
        flag=True
        exit()
if not flag:
    print(n+1)
        