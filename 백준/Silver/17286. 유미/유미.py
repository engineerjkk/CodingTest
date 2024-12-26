import sys
input = sys.stdin.readline
from itertools import permutations

X=[]
Y=[]
for _ in range(4):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

MIN=1e9
for permu in permutations([1,2,3],3):
    x,y=X[0],Y[0]

    tmp=0
    for i in permu:
        tmp+=(abs(x-X[i])**2+abs(y-Y[i])**2)**(0.5)
        x,y=X[i],Y[i]
    MIN=min(MIN,int(tmp))
print(MIN)

