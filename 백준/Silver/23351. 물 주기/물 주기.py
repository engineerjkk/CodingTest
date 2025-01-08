import sys 
input = sys.stdin.readline
from collections import deque  

n,k,a,b=map(int,input().split())

water=deque([k]*n) 

day=1

while True:
    
    for _ in range(a):
        water[0]+=b
        water.rotate(1)
    for _ in range(n):
        water[0]-=1
        if water[0]==0:
            print(day)
            exit()
        water.rotate(1)
    day+=1
