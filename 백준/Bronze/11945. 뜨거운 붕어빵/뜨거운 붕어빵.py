import sys
input = sys.stdin.readline

n,m=map(int,input().split())
lst=[]
for _ in range(n):
    a=input().strip()
    lst.append(a[::-1])
for i in range(n):
    print(lst[i])