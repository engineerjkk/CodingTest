import sys
input = sys.stdin.readline
k=int(input())
lst=[]
for _ in range(k):
    a=int(input())
    if a!=0:
        lst.append(a)
    else:
        lst.pop()
print(sum(lst))