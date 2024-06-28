def solution(N, stages):
    answer = []
    total=len(stages)
    dic={}
    for i in range(1,N+1):
        if total!=0:
            clear=stages.count(i)
            dic[i]=clear/total
            total-=clear
        else:
            dic[i]=0
    for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True):
        answer.append(key)   
    return answer