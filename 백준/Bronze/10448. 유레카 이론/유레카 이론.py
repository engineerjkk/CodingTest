import sys 
input = sys.stdin.readline 
from itertools import product 

t=int(input())

d=[0]*50 
d[0]=1
for i in range(1,50):
    d[i]=d[i-1]+i+1 

for _ in range(t):
    k=int(input())
    found=False
    for i in range(1,4):
        for pro in product(d,repeat=3):
            if sum(pro)==k:
                found=True
                break
        if found:
            break
    if found:
        print(1)
    else:
        print(0)


