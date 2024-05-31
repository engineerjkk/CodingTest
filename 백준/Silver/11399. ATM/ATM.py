import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
lst.sort()
answer=0
tmp=0
for i in lst:
    tmp+=i
    answer+=tmp
print(answer)