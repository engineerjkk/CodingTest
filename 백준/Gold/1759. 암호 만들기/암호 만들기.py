import sys
input = sys.stdin.readline
from itertools import combinations
L,C=map(int,input().split())
moum=["a","e","i","o",'u']
lst=list(map(str,input().split()))
lst.sort()
for nCr in combinations(lst,L):
    mo=0
    ja=0
    for x in nCr:
        if x in moum:
            mo+=1
        else:
            ja+=1
    if mo>=1 and ja>=2:
        print("".join(list(nCr)))
