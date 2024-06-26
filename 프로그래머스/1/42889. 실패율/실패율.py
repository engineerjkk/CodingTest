def solution(N, stages):
    result={}
    total=len(stages)
    answer=[]
    for i in range(1,N+1):
        if total!=0:
            clear=stages.count(i)
            result[i]=clear/total
            total-=clear
        else:
            result[i]=0
    for key,value in sorted(result.items(),key=lambda x:x[1],reverse=True):
        answer.append(key)
    return answer