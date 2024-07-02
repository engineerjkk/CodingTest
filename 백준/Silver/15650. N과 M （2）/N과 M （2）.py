from itertools import combinations
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
lst=[]
for i in range(1,n+1):
    lst.append(i)
for i in sorted(combinations(lst,m)):
    print(*i)
    
