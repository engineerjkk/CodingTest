def solution(dirs):
    sets=set()
    dic={"U":(1,0),"D":(-1,0),"L":(0,-1),"R":(0,1)}
    x,y=0,0
    for d in dirs:
        dx,dy=dic[d]
        nx=x+dx
        ny=y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            sets.add(((x,y),(nx,ny)))
            sets.add(((nx,ny),(x,y)))
            x,y=nx,ny
    return len(sets)//2