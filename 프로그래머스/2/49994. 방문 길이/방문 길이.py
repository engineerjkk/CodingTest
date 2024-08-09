def solution(dirs):
    dic={"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    x,y=0,0
    dic_set=set()
    for d in dirs:
        dx,dy=dic[d]
        nx,ny=x+dx,y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            dic_set.add(((x,y),(nx,ny)))
            dic_set.add(((nx,ny),(x,y)))
            x,y=nx,ny
    return len(dic_set)//2