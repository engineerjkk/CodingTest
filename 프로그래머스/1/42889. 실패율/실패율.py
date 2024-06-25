def solution(N, stages):
    result={}
    total=len(stages)
    for i in range(1,N+1):
        if total!=0:
            count=stages.count(i)
            result[i]=count/total
            total-=count
        else:
            result[i]=0
    lst=sorted(result.items(),key=lambda x:x[1],reverse=True)
    answer=[]
    for key, value in lst:
        answer.append(key)
    return answer