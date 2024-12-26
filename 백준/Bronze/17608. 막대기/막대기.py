import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

check=lst[-1]
cnt=1
for i in reversed(range(n-1)):
    if lst[i]>check:
        cnt+=1
        check=lst[i]
print(cnt)