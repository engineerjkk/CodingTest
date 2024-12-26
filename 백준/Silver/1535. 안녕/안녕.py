from itertools import combinations

N=int(input())
L=list(map(int,input().split()))
J=list(map(int,input().split()))
max_sum=0
for i in range(0,N+1):
    for combination in combinations(range(N),i):
        lsum=0
        jsum=0
        for j in combination:
            lsum+=L[j]
            jsum+=J[j]
        if lsum<100:
            max_sum=max(max_sum,jsum)
print(max_sum)