import sys
input = sys.stdin.readline

lst=[]
for _ in range(10):
    lst.append(int(input()))

tmp=[]
for i in range(10):
    tmp.append(lst[i]%42)

tmp2=list(set(tmp))
print(len(tmp2))