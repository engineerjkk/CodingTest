#import sys
#input = sys.stdin.readline

n,q=map(int,input().split())

alpha=list(input())

for _ in range(q):
    t,l,r=map(int,input().split())
    l-=1
    r-=1
    if t==1:
        count=0
        for i in range(l,r):
            if alpha[i] !=alpha[i+1]:
                count+=1
        print(count+1)
    if t==2:
        for i in range(l,r+1):
            id=ord(alpha[i])-ord('A')
            id=(id+1)%26
            alpha[i]=chr(id+ord('A'))