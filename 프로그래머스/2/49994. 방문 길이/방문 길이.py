def solution(dirs):
    answer = 0
    dic={'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)}
    def in_range(r,c):
        return -5<=r<=5 and -5<=c<=5
    r,c=0,0
    ans=set()
    for d in dirs:
        dr,dc=dic[d]
        if in_range(r+dr,c+dc):
            nr=r+dr
            nc=c+dc
            ans.add(((r,c),(nr,nc)))
            ans.add(((nr,nc),(r,c)))
            r=nr
            c=nc
    return len(ans)//2