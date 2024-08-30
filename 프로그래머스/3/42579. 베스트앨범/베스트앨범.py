def solution(genres, plays):
    answer = []
    dic1={}
    dic2={}
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g in dic1:
            dic1[g].append((i,p))
        else:
            dic1[g]=[(i,p)]
        if g in dic2:
            dic2[g]+=p
        else:
            dic2[g]=p
    for k,v in sorted(dic2.items(), key=lambda x:x[1],reverse=True):
        for i,num in sorted(dic1[k],key=lambda x:x[1],reverse=True)[:2]:
            answer.append(i)
    
    
    return answer