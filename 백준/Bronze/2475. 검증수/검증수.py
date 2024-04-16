import sys
input=sys.stdin.readline
lst=list(map(int,input().split()))
summation=0
for i in lst:
    summation+=(i**2)
print(int(summation%10))