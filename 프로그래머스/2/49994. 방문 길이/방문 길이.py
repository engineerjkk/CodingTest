def solution(dirs):
    answer = 0
    dic={"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    x,y=0,0
    nxt_set=set()
    for d in dirs:
        dx,dy=dic[d]
        nx=x+dx
        ny=y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            nxt_set.add(((x,y),(nx,ny)))
            nxt_set.add(((nx,ny),(x,y)))
            x,y=nx,ny
    return len(nxt_set)//2