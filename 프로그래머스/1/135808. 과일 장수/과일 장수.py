def solution(k, m, score):
    answer=0
    score=sorted(score,reverse=True)
    r=len(score)%m
    for i in range(0,len(score)-r,m):
        if score[i:i+m]:
            answer+=min(score[i:i+m])*m
    
    return answer

