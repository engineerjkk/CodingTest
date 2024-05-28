def solution(park, routes):

    def check(park, n, m, r, c, direction, cnt):
        if direction == "N":
            for i in range(1, cnt + 1):
                nr = r - i
                if nr < 0 or park[nr][c] == 'X':
                    return False
        elif direction == "S":
            for i in range(1, cnt + 1):
                nr = r + i
                if nr >= n or park[nr][c] == 'X':
                    return False
        elif direction == "W":
            for i in range(1, cnt + 1):
                nc = c - i
                if nc < 0 or park[r][nc] == 'X':
                    return False
        elif direction == "E":
            for i in range(1, cnt + 1):
                nc = c + i
                if nc >= m or park[r][nc] == 'X':
                    return False
        return True
    
    def move(park,n,m,r,c,direction,cnt):
        if direction=="N":
            nr=r-cnt
            nc=c
        elif direction=="S":
            nr=r+cnt
            nc=c
        elif direction=="W":
            nr=r
            nc=c-cnt
        elif direction=="E":
            nr=r
            nc=c+cnt 
        return nr,nc
    
    
    n=len(park)
    m=len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=="S":
                r,c=i,j
            
    for route in routes:
        direction,cnt=route.split()
        cnt=int(cnt)
        
        if check(park,n,m,r,c,direction,cnt)==True:
            r,c=move(park,n,m,r,c,direction,cnt)
        print(r,c)
    return [r,c]