def solution(N, stages):
    total=len(stages)
    answer=[]
    result={}
    for i in range(1,N+1):
        if total<=0:
            result[i]=0
        else:
            clear=stages.count(i)
            result[i]=clear/total
            total-=clear
    for key, value in sorted(result.items(),key=lambda x:x[1],reverse=True):
        answer.append(key)
    return answer
        
