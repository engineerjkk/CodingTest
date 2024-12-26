import sys
input = sys.stdin.readline
from itertools import combinations
lst=[]
for _ in range(9):
    lst.append(int(input()))

for nCr in combinations(lst,7):
    if sum(nCr)==100:
        break
for i in nCr:
    print(i)