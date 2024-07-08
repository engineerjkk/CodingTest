import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
MAX=0
for i in range(n):
    MAX=max(MAX,lst[i]*(i+1))
print(MAX)