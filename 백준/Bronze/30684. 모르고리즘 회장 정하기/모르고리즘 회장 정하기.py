import sys
input = sys.stdin.readline
n=int(input())
names=[]
for _ in range(n):
    name=input().strip()
    if len(name)==3:
        names.append(name)
names.sort()
print(names[0])