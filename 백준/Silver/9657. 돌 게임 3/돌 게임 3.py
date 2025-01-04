import sys
input = sys.stdin.readline 

n=int(input())

D=[False]*1001

D[1]=True
D[2]=False 
D[3]=True 
D[4]=True 

for i in range(5,1001):
    D[i] = (not D[i-1]) or (not D[i-3]) or (not D[i-4])

if D[n]:
    print("SK")
else:
    print("CY")