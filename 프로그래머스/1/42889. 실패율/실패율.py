def solution(N, stages):
    answer = []
    dic={}
    stages=sorted(stages)
    len_stages=len(stages)
    for i in range(1,N+1):
        dic[i]=0
    for i in range(1,N+1):
        if i not in stages:
            dic[i]=0
        else:
            fail=stages.count(i)
            dic[i]=fail/len_stages
            stages=stages[fail:]
            len_stages-=fail
    for key,value in sorted(dic.items(),key = lambda x:(x[1],-x[0]),reverse=True):
        answer.append(key)
    
        
    return answer