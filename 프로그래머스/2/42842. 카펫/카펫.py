def solution(brown, yellow):
    answer = []
    
    def check(x,y):
        tmp_y=x*y
        tmp_b=(x+2)*(y+2)-x*y
        if tmp_y==yellow and tmp_b==brown:
            return True
        else:
            return False
    
    for i in range(brown):
        for j in range(brown):
            if check(i,j):
                return sorted([i+2,j+2],reverse=True)
    return answer