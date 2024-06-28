import sys
input = sys.stdin.readline
n,k,b=map(int,input().split())
lst=[]
for _ in range(b):
    lst.append(int(input()))

a=0

tmp=[]
MAX=-sys.maxsize
for i in range(0,n+1):
    if i in lst:
        tmp.append(a)
    else:
        a+=1
        tmp.append(a)
left=0
right=k
while right<len(tmp):
    value=tmp[right]-tmp[left]
    MAX=max(MAX,value)
    left+=1
    right+=1
print(k-MAX)


