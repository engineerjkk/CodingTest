import sys
input = sys.stdin.readline
from itertools import combinations
import heapq
l,c=map(int,input().split())
alpha=['a','e','i','o','u']
lst=list(map(str,input().split()))
lst.sort()
answer=set()
pq=[]
for nCr in sorted(combinations(lst,l)):
    ja=0
    mo=0
    for x in nCr:
        if x not in alpha:
            ja+=1
        else:
            mo+=1
    if ja>=2 and mo>=1:
            print("".join(nCr))