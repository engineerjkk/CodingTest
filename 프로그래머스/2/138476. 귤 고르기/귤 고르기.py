def solution(k, tangerine):
    dic={}
    for i in tangerine:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    total=0
    answer=0
    for key,value in dic:
        k-=value
        answer+=1
        if k<=0:
            break
    return answer
