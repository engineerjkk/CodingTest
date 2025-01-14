import sys 
input = sys.stdin.readline 

m,n=map(int,input().split())
candy=[]
for _ in range(n):
    candy.append(int(input()))

candy.sort() 
cant=sum(candy)-m
answer=0
for i in range(n):
    tmp=min(candy[i],cant//(n-i))
    answer+=tmp**2
    cant-=tmp
print(answer%2**64)