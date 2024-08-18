from collections import deque

def in_range(r,c):
    return -1<r<5 and -1<c<5

def bfs(r,c,space):
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if in_range(nr,nc):
            if space[nr][nc]=='P':
                return False
            if space[nr][nc]=='O':
                for j in range(4):
                    nnr=nr+dr[j]
                    nnc=nc+dc[j]
                    if in_range(nnr,nnc) and space[nnr][nnc]=='P':
                        if nnr==r and nnc==c:
                            continue
                        return False
                        
    return True
        
    

def solution(places):
    answer=[]
    for place in places:
        space=[]
        for pla in place:
            space.append(list(map(str,pla.strip())))
        flag=True
        for i in range(5):
            for j in range(5):
                if space[i][j]=='P':
                    if not bfs(i,j,space):
                        flag=False
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer