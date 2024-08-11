from itertools import chain
def solution(n):   
    answer = [[None]*i for i in range(1,n+1)]
    [row,col,cnt]=[-1,0,1]
    for i in range(n):
        for _ in range(n-i):
            if i%3==0:
                row+=1
            elif i%3==1:
                col+=1
            else:
                row-=1
                col-=1
            answer[row][col]=cnt
            cnt+=1
    return list(chain(*answer))