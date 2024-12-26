import sys
input = sys.stdin.readline

n=int(input())

lst=[]
for i in range(n):
    lst.append(i+1)

while len(lst)>1:
    tmp=[]
    for i in range(len(lst)):
        if i%2!=0:
            tmp.append(lst[i])
    lst=tmp
    if len(lst)==1:
        break
print(lst[0])