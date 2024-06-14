import sys

def combinations(lst,r):
    def generate_combinations(lst,start,r,result,results):
        if r==0:
            results.append(result[:])
            return
        for i in range(start,len(lst)):
            result.append(lst[i])
            generate_combinations(lst,i+1,r-1,result,results)
            result.pop()
    results=[]
    generate_combinations(lst,0,r,[],results)
    return results

input = sys.stdin.readline
n,m = map(int,input().split())
space=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    space.append(tmp)

house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==1:
            house.append((i,j))
        elif space[i][j]==2:
            chicken.append((i,j))

nCr=combinations(chicken,m)
ans=2*n*2*n

def cal(chi):
    sm=0
    for hi,hj in house:
        nm=2*n
        for ci,cj in chi:
            nm=min(nm,abs(hi-ci)+abs(hj-cj))
        sm+=nm
    return sm
for chi in nCr:
    ans=min(ans,cal(chi))
print(ans)

