import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
MAX=0
for i in range(1,len(lst)+1):
    MAX=max(MAX,lst[i-1]*i)
print(MAX)
