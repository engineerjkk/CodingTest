def solution(dirs):
    dic={"U":(1,0),"D":(-1,0),"L":(0,-1),"R":(0,1)}
    x,y=5,5
    nxt_set=set()
    for d in dirs:
        dx,dy=dic[d]
        nx,ny=x+dx,y+dy
        nxt_set.add(((x,y),(nx,ny)))
        nxt_set.add(((nx,ny),(x,y)))
    return len(nxt_set)//2