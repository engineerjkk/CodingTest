import sys 
input = sys.stdin.readline 

n,m=map(int,input().split())

total_cost={}
for i in range(1,n+1):
    total_cost[i]=[int(input()),0]

for i in range(m):
    a=int(input())

    for fun,(cost,num) in total_cost.items():
        if cost<=a:
            total_cost[fun][1]+=1
            break
print(sorted(total_cost.items(),key=lambda x:x[1][1],reverse=True)[0][0])