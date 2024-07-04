import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

max_weight=0
for i in range(n):
    max_weight=max(max_weight,lst[i]*(i+1))
print(max_weight)