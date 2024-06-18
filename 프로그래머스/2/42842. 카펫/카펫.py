def solution(brown, yellow):
    
    def check(x,y):
        tmp_y=x*y
        tmp_b=2*x+2*y+4
        if tmp_y==yellow and tmp_b==brown:
            return True
        else:
            False
    for i in range(brown):
        for j in range(brown):
            if check(i,j):
                return sorted([i+2,j+2],reverse=True)
