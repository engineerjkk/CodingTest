def solution(genres, plays):
    answer = []
    dic1={}
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g not in dic1:
            dic1[g]=[(p,i)]
        else:
            dic1[g].append((p,i))
    dic2={}
    for g,p in zip(genres,plays):
        if g not in dic2:
            dic2[g]=p
        else:
            dic2[g]+=p
    
    for key,value in sorted(dic2.items(),key=lambda x:x[1],reverse=True):
        for p,i in sorted(dic1[key],key=lambda x:x[0],reverse=True)[:2]:
            answer.append(i)
    return answer