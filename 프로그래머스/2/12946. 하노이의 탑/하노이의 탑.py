def solution(n):
    answer=[]
    
    def hanoi(src,tar,inter,n):
        if n==1:
            answer.append([src,tar])
        else:
            hanoi(src,inter,tar,n-1)
            hanoi(src,tar,inter,1)
            hanoi(inter,tar,src,n-1)
    
    hanoi(1,3,2,n)
    return answer