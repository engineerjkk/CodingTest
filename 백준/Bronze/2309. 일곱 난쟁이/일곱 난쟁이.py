from itertools import combinations
import sys
input=sys.stdin.readline
lst=[]
for _ in range(9):
    lst.append(int(input()))

nCr=combinations(lst,7)
for x in nCr:
    if sum(x)==100:
        answer=list(x)
        break
answer.sort()
for i in answer:
    print(i)