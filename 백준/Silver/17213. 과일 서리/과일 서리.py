import sys 
input = sys.stdin.readline 
from itertools import combinations

n=int(input())
m=int(input())

ans=0
for nCr in combinations(list(range(1,m)),n-1):
    ans+=1
print(ans)