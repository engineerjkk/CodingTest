import sys
input = sys.stdin.readline
from itertools import combinations
n=int(input())


a=[]
for i in range(1,11):
    for nCr in combinations(list(reversed(range(10))),i):
        tmp=''
        for j in nCr:
            tmp+=str(j)
        a.append(int(tmp))

a.sort()
if len(a)<=n:
    print(-1)
else:
    print(a[n])