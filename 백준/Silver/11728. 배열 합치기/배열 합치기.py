import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
lst_n=list(map(int,input().split()))
lst_m=list(map(int,input().split()))

lst=sorted(lst_n+lst_m)
for i in lst:
    print(i,end=" ") 
